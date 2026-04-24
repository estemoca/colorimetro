let model = null;
let isModelLoaded = false;
let videoElement = null;
let overlayCanvas = null;
let overlayCtx = null;
let croppedCanvas = null;
let croppedCtx = null;
let captureCanvas = null;
let captureCtx = null;
let currentDetection = null;
let lastDetectionTime = 0;
let isDetecting = false;

const OBJECTS_TO_DETECT = ['banana', 'orange', 'apple', 'food', 'broccoli', 'pizza', 'cake', 'donut', 'hot dog'];
const DETECTION_INTERVAL = 150;
const MIN_DETECTION_INTERVAL = 100;

document.addEventListener('DOMContentLoaded', async () => {
    initializeElements();
    createCaptureCanvas();
    await loadModel();
    setupEventListeners();
    initializePlot();
    startRenderLoop();
});

function initializeElements() {
    videoElement = document.getElementById('video-stream');
    overlayCanvas = document.getElementById('overlay-canvas');
    overlayCtx = overlayCanvas.getContext('2d');
    croppedCanvas = document.getElementById('cropped-canvas');
    croppedCtx = croppedCanvas.getContext('2d');
}

function createCaptureCanvas() {
    captureCanvas = document.createElement('canvas');
    captureCanvas.width = 640;
    captureCanvas.height = 480;
    captureCtx = captureCanvas.getContext('2d', { willReadFrequently: true });
}

async function loadModel() {
    const statusEl = document.getElementById('mode-status');
    statusEl.textContent = 'Modo: Cargando modelo IA...';
    
    try {
        model = await cocoSsd.load({ base: 'lite_mobilenet_v2' });
        isModelLoaded = true;
        statusEl.textContent = 'Modo: IA lista';
        statusEl.classList.add('detecting');
    } catch (error) {
        console.error('Error cargando modelo:', error);
        statusEl.textContent = 'Modo: Sin IA (fallback color)';
    }
}

function startRenderLoop() {
    syncOverlaySize();
    requestAnimationFrame(detectAndRender);
}

async function detectAndRender(timestamp) {
    if (!videoElement || !videoElement.src) {
        requestAnimationFrame(detectAndRender);
        return;
    }

    captureCtx.drawImage(videoElement, 0, 0, 640, 480);

    if (isModelLoaded && !isDetecting && timestamp - lastDetectionTime > DETECTION_INTERVAL) {
        isDetecting = true;
        lastDetectionTime = timestamp;
        
        try {
            const predictions = await model.detect(captureCanvas);
            processDetections(predictions);
        } catch (error) {
            console.error('Error en detección:', error);
        }
        
        isDetecting = false;
    }

    drawOverlay();

    requestAnimationFrame(detectAndRender);
}

function processDetections(predictions) {
    let fruitDetected = null;
    let maxScore = 0;
    
    for (const pred of predictions) {
        const className = pred.class.toLowerCase();
        
        if (OBJECTS_TO_DETECT.some(obj => className.includes(obj))) {
            if (pred.score > maxScore) {
                maxScore = pred.score;
                fruitDetected = pred;
            }
        }
    }
    
    if (fruitDetected) {
        currentDetection = {
            bbox: fruitDetected.bbox,
            confidence: fruitDetected.score,
            class: fruitDetected.class,
            timestamp: Date.now()
        };
        
        updateDetectionUI(fruitDetected);
        updateCroppedPreview(fruitDetected);
    } else {
        currentDetection = null;
    }
    
    updateDetectionMode(fruitDetected !== null);
}

function drawOverlay() {
    overlayCtx.clearRect(0, 0, overlayCanvas.width, overlayCanvas.height);
    
    if (!currentDetection) return;
    
    const [x, y, width, height] = currentDetection.bbox;
    const scaleX = overlayCanvas.width / 640;
    const scaleY = overlayCanvas.height / 480;
    
    const drawX = x * scaleX;
    const drawY = y * scaleY;
    const drawW = width * scaleX;
    const drawH = height * scaleY;
    
    overlayCtx.strokeStyle = '#4CAF50';
    overlayCtx.lineWidth = 3;
    overlayCtx.strokeRect(drawX, drawY, drawW, drawH);
    
    overlayCtx.fillStyle = 'rgba(76, 175, 80, 0.2)';
    overlayCtx.fillRect(drawX, drawY, drawW, drawH);
    
    overlayCtx.fillStyle = '#4CAF50';
    overlayCtx.font = 'bold 13px Segoe UI, sans-serif';
    const label = `${currentDetection.class} ${Math.round(currentDetection.confidence * 100)}%`;
    const textWidth = overlayCtx.measureText(label).width;
    
    overlayCtx.fillStyle = 'rgba(76, 175, 80, 0.9)';
    overlayCtx.fillRect(drawX, drawY - 22, textWidth + 12, 20);
    overlayCtx.fillStyle = 'white';
    overlayCtx.fillText(label, drawX + 6, drawY - 7);
}

function updateDetectionUI(prediction) {
    document.getElementById('confidence').textContent = 
        `${Math.round(prediction.score * 100)}%`;
    document.getElementById('detection-area').textContent = 
        `${Math.round(prediction.bbox[2])}x${Math.round(prediction.bbox[3])} px`;
}

function updateDetectionMode(isIA) {
    const detectionMode = document.getElementById('detection-mode');
    if (isIA) {
        detectionMode.textContent = 'Detección: IA ✓';
        detectionMode.className = 'ai';
    } else {
        detectionMode.textContent = 'Detección: Color';
        detectionMode.className = 'color';
    }
}

function updateCroppedPreview(detection) {
    if (!detection) {
        croppedCtx.clearRect(0, 0, croppedCanvas.width, croppedCanvas.height);
        return;
    }
    
    const [x, y, width, height] = detection.bbox;
    
    const cropX = Math.max(0, x);
    const cropY = Math.max(0, y);
    const cropW = Math.min(width, 640 - cropX);
    const cropH = Math.min(height, 480 - cropY);
    
    croppedCtx.clearRect(0, 0, croppedCanvas.width, croppedCanvas.height);
    croppedCtx.drawImage(
        captureCanvas,
        cropX, cropY, cropW, cropH,
        0, 0, croppedCanvas.width, croppedCanvas.height
    );
}

function syncOverlaySize() {
    if (videoElement && overlayCanvas) {
        overlayCanvas.width = videoElement.clientWidth || 320;
        overlayCanvas.height = videoElement.clientHeight || 240;
    }
}

function setupEventListeners() {
    const analyzeBtn = document.getElementById('analyze-btn');
    analyzeBtn.addEventListener('click', analyzeImage);
    
    window.addEventListener('resize', () => {
        syncOverlaySize();
    });
    
    if (videoElement) {
        videoElement.addEventListener('loadedmetadata', syncOverlaySize);
    }
}

async function analyzeImage() {
    const analyzeBtn = document.getElementById('analyze-btn');
    const progressFill = document.getElementById('progress-fill');
    const progressText = document.getElementById('progress-text');
    
    analyzeBtn.disabled = true;
    analyzeBtn.textContent = '⏳ Analizando...';
    
    progressFill.style.width = '0%';
    progressText.textContent = '0%';
    
    try {
        captureCtx.drawImage(videoElement, 0, 0, 640, 480);
        
        progressFill.style.width = '20%';
        progressText.textContent = '20%';
        
        let imageData = captureCanvas.toDataURL('image/jpeg', 0.8);
        
        if (currentDetection && Date.now() - currentDetection.timestamp < 2000) {
            const [x, y, width, height] = currentDetection.bbox;
            
            const cropCanvas = document.createElement('canvas');
            cropCanvas.width = 320;
            cropCanvas.height = 240;
            const cropCtx = cropCanvas.getContext('2d');
            
            const cropX = Math.max(0, x);
            const cropY = Math.max(0, y);
            const cropW = Math.min(width, 640 - cropX);
            const cropH = Math.min(height, 480 - cropY);
            
            cropCtx.drawImage(captureCanvas, cropX, cropY, cropW, cropH, 0, 0, 320, 240);
            
            croppedCtx.clearRect(0, 0, croppedCanvas.width, croppedCanvas.height);
            croppedCtx.drawImage(cropCanvas, 0, 0, croppedCanvas.width, croppedCanvas.height);
            
            imageData = cropCanvas.toDataURL('image/jpeg', 0.85);
        }
        
        progressFill.style.width = '40%';
        progressText.textContent = '40%';
        
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: imageData }),
        });
        
        progressFill.style.width = '70%';
        progressText.textContent = '70%';
        
        const data = await response.json();
        
        if (data.error) {
            throw new Error(data.error);
        }
        
        document.getElementById('madurez-value').textContent = data.madurez;
        document.getElementById('rgb-value').textContent = 
            `R:${data.r} G:${data.g} B:${data.b}`;
        document.getElementById('brix-value').textContent = `${data.brix} °Bx`;
        document.getElementById('acidez-value').textContent = `${data.acidez} %`;
        
        if (data.cropped_image) {
            const img = new Image();
            img.onload = () => {
                croppedCtx.clearRect(0, 0, croppedCanvas.width, croppedCanvas.height);
                croppedCtx.drawImage(img, 0, 0, croppedCanvas.width, croppedCanvas.height);
            };
            img.src = 'data:image/jpeg;base64,' + data.cropped_image;
        }
        
        const gradoMatch = data.madurez.match(/Grado (\d)/);
        const grado = gradoMatch ? parseInt(gradoMatch[1]) : 0;
        const porcentaje = (grado / 5) * 100;
        
        progressFill.style.width = porcentaje + '%';
        progressText.textContent = Math.round(porcentaje) + '%';
        
        updatePlot(data.r, data.g, data.b);
        
    } catch (err) {
        console.error('Error en análisis:', err);
        document.getElementById('madurez-value').textContent = 'Error: ' + err.message;
    } finally {
        analyzeBtn.disabled = false;
        analyzeBtn.textContent = '🔬 ANALIZAR FRUTA';
    }
}

function initializePlot() {
    const defaultData = [{
        x: ['R', 'G', 'B'],
        y: [0, 0, 0],
        type: 'bar',
        marker: {
            color: ['#ff4444', '#44ff44', '#4444ff']
        }
    }];
    
    const layout = {
        title: {
            text: 'Firma Espectral del Mango',
            font: { color: '#4CAF50', size: 14 }
        },
        yaxis: { 
            range: [0, 255],
            title: 'Valor RGB',
            gridcolor: 'rgba(255,255,255,0.1)',
            titlefont: { color: '#888' },
            tickfont: { color: '#888' }
        },
        xaxis: {
            title: 'Canal',
            gridcolor: 'rgba(255,255,255,0.1)',
            titlefont: { color: '#888' },
            tickfont: { color: '#888' }
        },
        paper_bgcolor: 'transparent',
        plot_bgcolor: 'rgba(0,0,0,0.3)',
        margin: { t: 40, r: 20, b: 40, l: 50 },
        height: 200
    };
    
    Plotly.newPlot('plot-container', defaultData, layout);
}

function updatePlot(r, g, b) {
    const update = {
        y: [[r, g, b]]
    };
    
    Plotly.restyle('plot-container', update);
}
