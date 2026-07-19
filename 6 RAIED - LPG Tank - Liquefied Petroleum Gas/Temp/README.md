<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>RAIED | Realistic CDU Tower - Oil Refinery Style</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: 'Segoe UI', Arial, sans-serif; }
        
        .logo-container {
            position: absolute; top: 15px; left: 50%; transform: translateX(-50%);
            z-index: 250; text-align: center; pointer-events: none;
            background: rgba(0,0,0,0.75); backdrop-filter: blur(10px);
            padding: 6px 20px;
            border-radius: 50px;
            border: 1px solid rgba(255,200,100,0.7);
        }
        .logo-acronym { font-size: 1.3rem; color: #ffaa44; font-weight: 900; }
        .logo-full { font-size: 0.55rem; color: #e0e0e0; letter-spacing: 1.5px; }
        
        #info {
            position: absolute; top: 20px; left: 20px; z-index: 200;
            background: rgba(0,0,0,0.7); backdrop-filter: blur(8px);
            color: white; padding: 4px 10px;
            border-radius: 8px;
            border-left: 3px solid #ff8844;
            font-family: monospace;
            pointer-events: none;
            font-size: 0.55rem;
        }
        #info h1 { font-size: 0.8rem; margin: 0; }
        #info p { margin: 2px 0 0 0; font-size: 0.55rem; }
        
        .controls-panel {
            position: absolute; bottom: 20px; right: 20px;
            z-index: 300;
            background: rgba(10,20,28,0.95);
            backdrop-filter: blur(12px);
            border-radius: 12px;
            padding: 10px 12px;
            color: white;
            font-family: monospace;
            border: 1px solid rgba(255,180,70,0.5);
            min-width: 280px;
            max-width: 550px;
            min-height: 350px;
            width: 340px;
            height: auto;
            text-align: center;
            cursor: grab;
            user-select: none;
            font-size: 0.65rem;
            overflow: auto;
            resize: both;
        }
        .controls-panel:active { cursor: grabbing; }
        
        .controls-panel::-webkit-resizer {
            background: linear-gradient(135deg, transparent 50%, #ffaa66 50%);
            border-radius: 0 0 12px 0;
        }
        
        .resize-handle {
            position: absolute;
            bottom: 0;
            right: 0;
            width: 18px;
            height: 18px;
            background: linear-gradient(135deg, transparent 70%, #ffaa66 70%);
            cursor: nw-resize;
            border-radius: 0 0 12px 0;
            z-index: 310;
            pointer-events: auto;
        }
        .resize-handle:hover {
            background: linear-gradient(135deg, transparent 70%, #ff8844 70%);
            width: 20px;
            height: 20px;
        }
        
        .resize-hint {
            position: absolute;
            bottom: 2px;
            right: 22px;
            font-size: 0.45rem;
            color: #ffaa66;
            opacity: 0.7;
            pointer-events: none;
            z-index: 311;
        }
        
        .panel-header { 
            display: flex; 
            justify-content: space-between; 
            margin-bottom: 8px; 
            padding-bottom: 4px; 
            border-bottom: 1px solid #ffaa5544; 
            cursor: grab;
            font-size: 0.7rem;
        }
        .reset-pos-btn { 
            background: #2c5a6e; 
            border: none; 
            color: #aaa; 
            padding: 2px 6px; 
            border-radius: 12px; 
            cursor: pointer;
            font-size: 0.55rem;
        }
        .reset-pos-btn:hover { background: #ff8844; color: white; }
        
        .status-panel { 
            background: #000000aa; 
            border-radius: 12px; 
            padding: 4px 8px; 
            margin: 6px 0; 
        }
        .progress-bar { width: 100%; height: 8px; background: #1e3a3f; border-radius: 10px; overflow: hidden; margin: 3px 0; }
        .progress-fill { width: 0%; height: 100%; background: linear-gradient(90deg, #ff9933, #ffdd66); border-radius: 10px; transition: width 0.05s linear; }
        .status-led { display: flex; align-items: center; justify-content: center; gap: 6px; margin: 4px 0; }
        .led { width: 8px; height: 8px; border-radius: 50%; background: #ff3a3a; box-shadow: 0 0 6px red; transition: all 0.2s; }
        
        button {
            background: #2c5a6e;
            border: none;
            color: white;
            padding: 4px 8px;
            margin: 2px;
            border-radius: 16px;
            cursor: pointer;
            font-weight: bold;
            font-family: monospace;
            font-size: 0.6rem;
            transition: all 0.1s ease;
        }
        button:hover { filter: brightness(1.15); transform: scale(1.02); }
        .btn-primary { background: #d95b1c; }
        .btn-danger { background: #b13e3e; }
        .btn-warning { background: #e68a2e; }
        .btn-drone { background: #2a6a5a; animation: pulseGreen 1s infinite; }
        .btn-drone-off { background: #4a6a7a; }
        @keyframes pulseGreen { 0% { box-shadow: 0 0 0px #44ff88; } 100% { box-shadow: 0 0 6px #44ff88; } }
        
        .separator { height: 1px; background: #ffaa5544; margin: 6px 0; }
        .locations-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 3px; margin: 5px 0; }
        .loc-btn { background: #5a3a2a; font-size: 0.55rem; padding: 2px 4px; }
        .loc-btn-normal { background: #2a5a3a; }
        .loc-btn-threat { background: #8a3a2a; }
        h3 { margin: 4px 0; font-size: 0.7rem; color: #ffaa66; }
        .impact-notice { color: #ff8866; font-size: 0.5rem; margin-top: 4px; }
        .instruction-toast { 
            position: absolute; bottom: 15px; left: 15px; 
            background: rgba(0,0,0,0.6); 
            padding: 4px 10px; 
            border-radius: 16px; 
            font-size: 0.55rem; 
            color: #ccc; 
            font-family: monospace; 
            pointer-events: none; 
            z-index: 200; 
        }
        
        .badge-group { font-size: 0.5rem; background: #2a4a55; border-radius: 10px; padding: 2px 6px; margin-top: 4px; display: inline-block; }
        .section-title { background: #2a4a55; border-radius: 8px; padding: 3px; margin: 5px 0 3px 0; font-size: 0.6rem; font-weight: bold; }
        .drone-status { background: #1a3a3a; border-radius: 8px; padding: 4px; margin: 5px 0; font-size: 0.55rem; }
        
        .controls-panel::-webkit-scrollbar { width: 6px; height: 6px; }
        .controls-panel::-webkit-scrollbar-track { background: #1a2a3a; border-radius: 3px; }
        .controls-panel::-webkit-scrollbar-thumb { background: #ffaa66; border-radius: 3px; }
        
        @keyframes pulseRed { 0% { box-shadow: 0 0 0px #ff4444; } 100% { box-shadow: 0 0 8px #ff4444; } }
    </style>
</head>
<body>
    <div class="logo-container">
        <div class="logo-acronym">RAIED</div>
        <div class="logo-full">REFINERY ANTI-DRONE INTERCEPTION ENVIRONMENT DOME</div>
    </div>
    
    <div id="info">
        <h1>🏭 REALISTIC CDU TOWER | <span class="highlight">Atmospheric Crude Distillation Unit</span></h1>
        <p>Fractionating trays | Platforms | Piping | Ladders | Industrial refinery design</p>
    </div>
    
    <div class="controls-panel" id="movablePanel">
        <div class="resize-handle" id="resizeHandle"></div>
        <div class="resize-hint">◢ resize</div>
        <div class="panel-header" id="dragHandle">
            <span>⋮⋮ RAIED CONTROL ⋮⋮</span>
            <button class="reset-pos-btn" id="resetPanelPos">⟳</button>
        </div>
        
        <div class="threat-badge" style="background:#cc4444cc; border-radius:12px; padding:2px 8px; margin-bottom:5px;">⚠️ RAIED ACTIVE</div>
        
        <div class="status-panel">
            <div>🚪 VERTICAL DOORS <span id="sidePercent">0%</span><div class="progress-bar"><div class="progress-fill" id="sideFill"></div></div></div>
            <div>🔘 TOP STEEL SHUTTERS <span id="shutterPercent">0%</span><div class="progress-bar"><div class="progress-fill" id="shutterFill"></div></div></div>
            <div class="status-led"><div class="led" id="threatLed"></div><span id="threatText">NORMAL MODE</span></div>
        </div>
        
        <div class="button-group">
            <button id="raiseSideBtn" class="btn-primary">▲ CLOSE DOORS</button>
            <button id="lowerSideBtn">▼ OPEN DOORS</button>
            <button id="extendAllShuttersBtn" class="btn-warning">🔒 EXTEND SHUTTERS</button>
            <button id="retractAllShuttersBtn">🔓 RETRACT SHUTTERS</button>
            <button id="emergencyFullBtn" style="background:#b83b2e;">🚨 FULL SEAL</button>
            <button id="resetShieldsBtn">⟳ RESET</button>
        </div>
        
        <div class="separator"></div>
        
        <h3>🛸 DRONE CONTROL</h3>
        <div class="drone-status">
            <div class="button-group">
                <button id="spawnDroneNormalBtn" class="btn-drone">🛸 NORMAL DRONE</button>
                <button id="spawnDroneThreatBtn" style="background:#8a3a2a; animation:pulseRed 1s infinite;">💀 THREAT DRONE</button>
                <button id="removeDroneBtn" class="btn-drone-off">❌ REMOVE DRONE</button>
                <button id="droneStrikeBtn" style="background:#ff8844;">💥 DRONE STRIKE</button>
            </div>
            <div id="droneStatus" style="margin-top:4px; font-size:0.55rem;">⚡ No drone active</div>
        </div>
        
        <div class="separator"></div>
        
        <div class="section-title">🔥 NORMAL MODE STRIKES (Doors Open Required)</div>
        <div class="locations-grid">
            <button id="strikeNormal1" class="loc-btn loc-btn-normal">🔥 Bottom Section</button>
            <button id="strikeNormal2" class="loc-btn loc-btn-normal">🔥 Lower Trays</button>
            <button id="strikeNormal3" class="loc-btn loc-btn-normal">🔥 Mid Trays</button>
            <button id="strikeNormal4" class="loc-btn loc-btn-normal">🔥 Upper Trays</button>
            <button id="strikeNormal5" class="loc-btn loc-btn-normal">🔥 Top Section</button>
            <button id="strikeNormal6" class="loc-btn loc-btn-normal">🔥 Overhead</button>
        </div>
        
        <div class="section-title">💀 THREAT MODE STRIKES (Shutters Extended Required)</div>
        <div class="locations-grid">
            <button id="strikeThreat1" class="loc-btn loc-btn-threat">💀 Top Dome</button>
            <button id="strikeThreat2" class="loc-btn loc-btn-threat">💀 East Platform</button>
            <button id="strikeThreat3" class="loc-btn loc-btn-threat">💀 North Piping</button>
            <button id="strikeThreat4" class="loc-btn loc-btn-threat">💀 South Piping</button>
            <button id="strikeThreat5" class="loc-btn loc-btn-threat">💀 West Platform</button>
            <button id="strikeThreat6" class="loc-btn loc-btn-threat">💀 Manway</button>
        </div>
        
        <div class="separator"></div>
        
        <button id="resetAllActionsBtn" style="background:#8a3a2a; width:100%; margin-top:5px;">🔄 RESET EVERYTHING 🔄</button>
        <div class="impact-notice" id="impactMessage">⚡ Realistic CDU Tower with fractionating trays, platforms, and piping</div>
        <div class="badge-group">🏭 Crude Distillation Unit | 40+ Trays | Industrial Refinery Design</div>
    </div>
    
    <div class="instruction-toast">✅ REALISTIC CDU TOWER | Fractionating trays | Platforms | Piping | Ladders | Industrial design</div>

    <script type="importmap">
        { "imports": { "three": "https://unpkg.com/three@0.128.0/build/three.module.js", "three/addons/": "https://unpkg.com/three@0.128.0/examples/jsm/" } }
    </script>

    <script type="module">
        import * as THREE from 'three';
        import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
        import { CSS2DRenderer } from 'three/addons/renderers/CSS2DRenderer.js';

        // --- Scene Setup ---
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x0a1a2a);
        scene.fog = new THREE.FogExp2(0x0a1a2a, 0.002);
        
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        document.body.appendChild(renderer.domElement);
        
        const labelRenderer = new CSS2DRenderer();
        labelRenderer.setSize(window.innerWidth, window.innerHeight);
        labelRenderer.domElement.style.position = 'absolute';
        labelRenderer.domElement.style.top = '0px';
        labelRenderer.domElement.style.left = '0px';
        labelRenderer.domElement.style.pointerEvents = 'none';
        document.body.appendChild(labelRenderer.domElement);
        
        const camera = new THREE.PerspectiveCamera(40, window.innerWidth / window.innerHeight, 0.1, 200);
        camera.position.set(18, 12, 22);
        camera.lookAt(0, 7, 0);
        
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.target.set(0, 7, 0);
        controls.zoomSpeed = 1.2;
        
        // --- Lighting ---
        const ambient = new THREE.AmbientLight(0x404060, 0.55);
        scene.add(ambient);
        const keyLight = new THREE.DirectionalLight(0xffeedd, 1.3);
        keyLight.position.set(7, 15, 6);
        keyLight.castShadow = true;
        keyLight.shadow.mapSize.width = 1024;
        keyLight.shadow.mapSize.height = 1024;
        scene.add(keyLight);
        const fill = new THREE.PointLight(0x5588aa, 0.5);
        fill.position.set(0, 6, 0);
        scene.add(fill);
        const rim = new THREE.PointLight(0xffaa66, 0.55);
        rim.position.set(-7, 7, -9);
        scene.add(rim);
        const topLight = new THREE.PointLight(0xffaa88, 0.4);
        topLight.position.set(0, 13, 0);
        scene.add(topLight);
        
        // Ground
        const ground = new THREE.Mesh(new THREE.PlaneGeometry(55, 55), new THREE.MeshStandardMaterial({ color: 0x3a4048, roughness: 0.85, metalness: 0.1 }));
        ground.rotation.x = -Math.PI / 2;
        ground.position.y = -0.4;
        ground.receiveShadow = true;
        scene.add(ground);
        
        const gridHelper = new THREE.GridHelper(55, 36, 0x88aacc, 0x446688);
        gridHelper.position.y = -0.35;
        gridHelper.material.transparent = true;
        gridHelper.material.opacity = 0.22;
        scene.add(gridHelper);
        
        // ==================== REALISTIC CDU TOWER ====================
        const towerGroup = new THREE.Group();
        
        // Main column body - tapered at top
        const colRadiusBottom = 1.45;
        const colRadiusTop = 1.05;
        const colHeight = 9.2;
        
        const shellMat = new THREE.MeshStandardMaterial({ color: 0x9aaeaa, metalness: 0.85, roughness: 0.22 });
        const mainColumn = new THREE.Mesh(new THREE.CylinderGeometry(colRadiusTop, colRadiusBottom, colHeight, 64, 64), shellMat);
        mainColumn.castShadow = true;
        mainColumn.receiveShadow = true;
        mainColumn.position.y = colHeight / 2;
        towerGroup.add(mainColumn);
        
        // ==================== FRACTIONATING TRAYS (40+ trays) ====================
        const trayMat = new THREE.MeshStandardMaterial({ color: 0xbcac78, metalness: 0.75, roughness: 0.35 });
        const numTrays = 42;
        
        for (let i = 1; i <= numTrays; i++) {
            const yPos = i * (colHeight / (numTrays + 1)) + 0.15;
            const trayRadius = colRadiusBottom - (colRadiusBottom - colRadiusTop) * (yPos / colHeight);
            const trayRing = new THREE.Mesh(new THREE.TorusGeometry(trayRadius + 0.08, 0.055, 32, 100), trayMat);
            trayRing.rotation.x = Math.PI / 2;
            trayRing.position.y = yPos;
            trayRing.castShadow = true;
            towerGroup.add(trayRing);
            
            // Add tray support rings every few trays
            if (i % 6 === 0) {
                const supportRing = new THREE.Mesh(new THREE.TorusGeometry(trayRadius + 0.12, 0.07, 32, 100), 
                    new THREE.MeshStandardMaterial({ color: 0xccaa77, metalness: 0.82 }));
                supportRing.rotation.x = Math.PI / 2;
                supportRing.position.y = yPos - 0.08;
                supportRing.castShadow = true;
                towerGroup.add(supportRing);
            }
        }
        
        // ==================== PLATFORMS (Walkways at different levels) ====================
        const platformMat = new THREE.MeshStandardMaterial({ color: 0x8a8e7a, metalness: 0.6, roughness: 0.5 });
        const railMat = new THREE.MeshStandardMaterial({ color: 0xccaa77, metalness: 0.7 });
        
        const platformLevels = [1.8, 3.5, 5.2, 6.9, 8.2];
        const platformAngles = [0, Math.PI/2, Math.PI, 3*Math.PI/2];
        
        platformLevels.forEach((yPos, idx) => {
            const radius = colRadiusBottom - (colRadiusBottom - colRadiusTop) * (yPos / colHeight);
            
            platformAngles.forEach(angle => {
                const xOffset = Math.cos(angle) * (radius + 0.45);
                const zOffset = Math.sin(angle) * (radius + 0.45);
                
                // Platform base
                const platform = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.08, 1.2), platformMat);
                platform.position.set(xOffset, yPos, zOffset);
                platform.castShadow = true;
                towerGroup.add(platform);
                
                // Railing posts
                for (let p = -0.5; p <= 0.5; p += 1.0) {
                    for (let q = -0.5; q <= 0.5; q += 1.0) {
                        if (Math.abs(p) + Math.abs(q) > 0.5) {
                            const post = new THREE.Mesh(new THREE.BoxGeometry(0.05, 0.35, 0.05), railMat);
                            post.position.set(xOffset + p * 0.6, yPos + 0.12, zOffset + q * 0.6);
                            post.castShadow = true;
                            towerGroup.add(post);
                        }
                    }
                }
                
                // Railing horizontal bars
                const railBar = new THREE.Mesh(new THREE.BoxGeometry(1.25, 0.04, 0.04), railMat);
                railBar.position.set(xOffset, yPos + 0.2, zOffset);
                railBar.castShadow = true;
                towerGroup.add(railBar);
            });
        });
        
        // ==================== PIPING AND TUBING ====================
        const pipeMat = new THREE.MeshStandardMaterial({ color: 0xccaa88, metalness: 0.78, roughness: 0.3 });
        
        // Vertical pipes along tower
        const pipePositions = [
            { angle: 0.3, radius: 1.65, startY: 0.2, endY: 8.8, diameter: 0.12 },
            { angle: 2.0, radius: 1.7, startY: 0.2, endY: 8.5, diameter: 0.1 },
            { angle: 3.8, radius: 1.68, startY: 0.2, endY: 9.0, diameter: 0.13 },
            { angle: 5.0, radius: 1.72, startY: 0.2, endY: 8.3, diameter: 0.11 }
        ];
        
        pipePositions.forEach(pipe => {
            const xPos = Math.cos(pipe.angle) * pipe.radius;
            const zPos = Math.sin(pipe.angle) * pipe.radius;
            const pipeLength = pipe.endY - pipe.startY;
            const pipeMesh = new THREE.Mesh(new THREE.CylinderGeometry(pipe.diameter, pipe.diameter, pipeLength, 12), pipeMat);
            pipeMesh.position.set(xPos, pipe.startY + pipeLength/2, zPos);
            pipeMesh.castShadow = true;
            towerGroup.add(pipeMesh);
        });
        
        // Horizontal connecting pipes at platform levels
        platformLevels.forEach(yPos => {
            const radius = colRadiusBottom - (colRadiusBottom - colRadiusTop) * (yPos / colHeight);
            for (let a = 0; a < Math.PI * 2; a += Math.PI / 3) {
                const x1 = Math.cos(a) * radius;
                const z1 = Math.sin(a) * radius;
                const x2 = Math.cos(a + 0.5) * (radius + 0.55);
                const z2 = Math.sin(a + 0.5) * (radius + 0.55);
                
                const pipeHoriz = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.07, 0.8, 8), pipeMat);
                pipeHoriz.position.set((x1 + x2)/2, yPos + 0.15, (z1 + z2)/2);
                pipeHoriz.rotation.z = Math.atan2(z2 - z1, x2 - x1);
                pipeHoriz.castShadow = true;
                towerGroup.add(pipeHoriz);
            }
        });
        
        // ==================== LADDER (Industrial access ladder) ====================
        const ladderMat = new THREE.MeshStandardMaterial({ color: 0xaa8866, metalness: 0.55 });
        const ladderX = 1.55;
        const ladderZ = 1.55;
        
        for (let step = 0; step < 40; step++) {
            const yPos = 0.3 + step * 0.22;
            if (yPos < 8.5) {
                const rung = new THREE.Mesh(new THREE.BoxGeometry(0.45, 0.04, 0.06), ladderMat);
                rung.position.set(ladderX, yPos, ladderZ);
                rung.castShadow = true;
                towerGroup.add(rung);
            }
        }
        
        // Ladder rails
        const railLeft = new THREE.Mesh(new THREE.BoxGeometry(0.06, 8.2, 0.06), ladderMat);
        railLeft.position.set(ladderX - 0.22, 4.2, ladderZ);
        railLeft.castShadow = true;
        towerGroup.add(railLeft);
        
        const railRight = new THREE.Mesh(new THREE.BoxGeometry(0.06, 8.2, 0.06), ladderMat);
        railRight.position.set(ladderX + 0.22, 4.2, ladderZ);
        railRight.castShadow = true;
        towerGroup.add(railRight);
        
        // ==================== DOME TOP WITH MANWAY ====================
        const domeMat = new THREE.MeshStandardMaterial({ color: 0xc8bc8a, metalness: 0.7, roughness: 0.25 });
        const topDome = new THREE.Mesh(new THREE.SphereGeometry(1.08, 48, 48, 0, Math.PI * 2, 0, Math.PI / 2.5), domeMat);
        topDome.position.y = colHeight + 0.08;
        topDome.castShadow = true;
        towerGroup.add(topDome);
        
        // Manway (access hatch) on top
        const manway = new THREE.Mesh(new THREE.CylinderGeometry(0.45, 0.45, 0.12, 16), new THREE.MeshStandardMaterial({ color: 0xddbb88, metalness: 0.75 }));
        manway.position.set(0.6, colHeight + 0.45, 0.6);
        manway.castShadow = true;
        towerGroup.add(manway);
        
        const manwayCover = new THREE.Mesh(new THREE.CylinderGeometry(0.48, 0.48, 0.06, 16), new THREE.MeshStandardMaterial({ color: 0xeecc99, metalness: 0.8 }));
        manwayCover.position.set(0.6, colHeight + 0.51, 0.6);
        manwayCover.castShadow = true;
        towerGroup.add(manwayCover);
        
        // ==================== PRESSURE RELIEF VALVE ====================
        const prValve = new THREE.Mesh(new THREE.CylinderGeometry(0.28, 0.35, 0.4, 12), new THREE.MeshStandardMaterial({ color: 0xdd8844, metalness: 0.85 }));
        prValve.position.set(-0.55, colHeight + 0.55, -0.55);
        prValve.castShadow = true;
        towerGroup.add(prValve);
        
        // ==================== INSTRUMENTATION (Gauges and sensors) ====================
        const gaugeMat = new THREE.MeshStandardMaterial({ color: 0x88aacc, metalness: 0.7, emissive: 0x224466 });
        
        const gaugeLevels = [2.5, 4.8, 7.2];
        gaugeLevels.forEach(yPos => {
            const gauge = new THREE.Mesh(new THREE.SphereGeometry(0.12, 16, 16), gaugeMat);
            gauge.position.set(1.25, yPos, 1.25);
            gauge.castShadow = true;
            towerGroup.add(gauge);
            
            const gauge2 = new THREE.Mesh(new THREE.SphereGeometry(0.12, 16, 16), gaugeMat);
            gauge2.position.set(-1.35, yPos, -1.25);
            gauge2.castShadow = true;
            towerGroup.add(gauge2);
        });
        
        // ==================== INSULATION JACKETING (Refinery typical) ====================
        const insulationMat = new THREE.MeshStandardMaterial({ color: 0x7a8a7e, metalness: 0.45, roughness: 0.6 });
        for (let i = 1; i <= 8; i++) {
            const yStart = i * 1.05;
            const band = new THREE.Mesh(new THREE.TorusGeometry(colRadiusBottom - 0.05, 0.045, 16, 100), insulationMat);
            band.rotation.x = Math.PI / 2;
            band.position.y = yStart;
            band.castShadow = true;
            towerGroup.add(band);
        }
        
        scene.add(towerGroup);
        
        // ==================== SQUARE FRAME (4 Pillars) ====================
        const SQUARE_SIZE = 14.0;
        const HALF_SIZE = SQUARE_SIZE / 2;
        
        const PILLAR_WIDTH = 0.6;
        const PILLAR_DEPTH = 0.6;
        const PILLAR_H = colHeight + 3.0;
        const TOP_Y = PILLAR_H;
        
        const pillarMatObj = new THREE.MeshStandardMaterial({ color: 0x8a8e7a, metalness: 0.65, roughness: 0.3 });
        const pillarPositions = [
            { x: -HALF_SIZE, z: -HALF_SIZE },
            { x:  HALF_SIZE, z: -HALF_SIZE },
            { x:  HALF_SIZE, z:  HALF_SIZE },
            { x: -HALF_SIZE, z:  HALF_SIZE }
        ];
        
        pillarPositions.forEach(pos => {
            const pillar = new THREE.Mesh(new THREE.BoxGeometry(PILLAR_WIDTH, PILLAR_H, PILLAR_DEPTH), pillarMatObj);
            pillar.position.set(pos.x, PILLAR_H / 2, pos.z);
            pillar.castShadow = true;
            pillar.receiveShadow = true;
            scene.add(pillar);
        });
        
        // ==================== 4 RSJ BARS ====================
        const rsjMat = new THREE.MeshStandardMaterial({ color: 0xccaa77, metalness: 0.88, roughness: 0.25 });
        const BAR_WIDTH = PILLAR_WIDTH;
        const BAR_DEPTH = PILLAR_DEPTH;
        const BAR_HEIGHT = 0.6;
        
        const southBar = new THREE.Mesh(new THREE.BoxGeometry(SQUARE_SIZE, BAR_HEIGHT, BAR_DEPTH), rsjMat);
        southBar.position.set(0, TOP_Y, -HALF_SIZE);
        southBar.castShadow = true;
        scene.add(southBar);
        
        const eastBar = new THREE.Mesh(new THREE.BoxGeometry(BAR_WIDTH, BAR_HEIGHT, SQUARE_SIZE), rsjMat);
        eastBar.position.set(HALF_SIZE, TOP_Y, 0);
        eastBar.castShadow = true;
        scene.add(eastBar);
        
        const northBar = new THREE.Mesh(new THREE.BoxGeometry(SQUARE_SIZE, BAR_HEIGHT, BAR_DEPTH), rsjMat);
        northBar.position.set(0, TOP_Y, HALF_SIZE);
        northBar.castShadow = true;
        scene.add(northBar);
        
        const westBar = new THREE.Mesh(new THREE.BoxGeometry(BAR_WIDTH, BAR_HEIGHT, SQUARE_SIZE), rsjMat);
        westBar.position.set(-HALF_SIZE, TOP_Y, 0);
        westBar.castShadow = true;
        scene.add(westBar);
        
        // Corner connectors
        const connectorMat = new THREE.MeshStandardMaterial({ color: 0xddbb88, metalness: 0.85 });
        const cornerPositions = [
            { x: -HALF_SIZE, z: -HALF_SIZE },
            { x:  HALF_SIZE, z: -HALF_SIZE },
            { x:  HALF_SIZE, z:  HALF_SIZE },
            { x: -HALF_SIZE, z:  HALF_SIZE }
        ];
        
        cornerPositions.forEach(pos => {
            const connector = new THREE.Mesh(new THREE.BoxGeometry(0.7, BAR_HEIGHT + 0.1, 0.7), connectorMat);
            connector.position.set(pos.x, TOP_Y, pos.z);
            connector.castShadow = true;
            scene.add(connector);
        });
        
        // ==================== 4 PARALLEL BEADING BARS ====================
        const beadingMat = new THREE.MeshStandardMaterial({ color: 0xccaa88, metalness: 0.82, roughness: 0.3 });
        const BEADING_WIDTH = 0.12;
        const BEADING_HEIGHT = 0.12;
        
        const beadingXPositions = [-4.2, -1.4, 1.4, 4.2];
        const beadingLength = SQUARE_SIZE;
        
        beadingXPositions.forEach((xPos) => {
            const beadingBar = new THREE.Mesh(new THREE.BoxGeometry(BEADING_WIDTH, BEADING_HEIGHT, beadingLength), beadingMat);
            beadingBar.position.set(xPos, TOP_Y + 0.05, 0);
            beadingBar.castShadow = true;
            scene.add(beadingBar);
        });
        
        // ==================== 5 TRACKS OF WIDE STEEL SHUTTERS ====================
        const SECTION_LENGTH = SQUARE_SIZE / 4;
        const SHUTTER_THICK = 0.016;
        
        const shutterTracks = [
            { centerX: -5.6, width: 2.8 },
            { centerX: -2.8, width: 2.8 },
            { centerX: 0, width: 2.8 },
            { centerX: 2.8, width: 2.8 },
            { centerX: 5.6, width: 2.8 }
        ];
        
        const steelMat = new THREE.MeshStandardMaterial({ color: 0x8a9a8a, metalness: 0.92, roughness: 0.25, emissive: 0x111111 });
        
        let shutterExtension = 0;
        
        shutterTracks.forEach((track) => {
            for (let i = 0; i < 4; i++) {
                const shutter = new THREE.Mesh(new THREE.BoxGeometry(track.width, SHUTTER_THICK, SECTION_LENGTH), steelMat);
                const sectionStartZ = -HALF_SIZE + (i * SECTION_LENGTH);
                const sectionCenterZ = sectionStartZ + (SECTION_LENGTH / 2);
                const retractedZ = -HALF_SIZE;
                const extendedZ = sectionCenterZ;
                const stackOffsetY = i * 0.018;
                shutter.position.set(track.centerX, TOP_Y + 0.1 + stackOffsetY, retractedZ);
                shutter.castShadow = true;
                shutter.receiveShadow = true;
                scene.add(shutter);
                
                shutter.userData = {
                    retractedZ: retractedZ,
                    extendedZ: extendedZ,
                    stackOffsetY: stackOffsetY
                };
            }
        });
        
        function updateAllShutters(factor) {
            shutterExtension = Math.min(1, Math.max(0, factor));
            
            scene.children.forEach(child => {
                if (child.isMesh && child.material && child.geometry.parameters && 
                    child.geometry.parameters.width === 2.8 && child.position.y > TOP_Y) {
                    const targetZ = child.userData.retractedZ + (child.userData.extendedZ - child.userData.retractedZ) * shutterExtension;
                    const yOffset = (1 - shutterExtension) * child.userData.stackOffsetY;
                    child.position.z = targetZ;
                    child.position.y = TOP_Y + 0.1 + yOffset;
                }
            });
            
            const percent = Math.floor(shutterExtension * 100);
            document.getElementById('shutterPercent').innerText = `${percent}%`;
            document.getElementById('shutterFill').style.width = `${shutterExtension * 100}%`;
            updateThreatDisplay();
            if (typeof updateStrikeButtonsState === 'function') updateStrikeButtonsState();
        }
        
        function animateShutters(target) {
            const start = shutterExtension;
            const startTime = performance.now();
            function step(now) {
                const t = Math.min(1, (now - startTime) / 600);
                updateAllShutters(start + (target - start) * t);
                if (t < 1) requestAnimationFrame(step);
            }
            requestAnimationFrame(step);
        }
        
        // ==================== VERTICAL DOORS ====================
        const DOOR_WIDTH = SQUARE_SIZE / 4;
        const DOOR_HEIGHT = PILLAR_H - 0.5;
        const DOOR_Y = DOOR_HEIGHT / 2;
        const STACK_OFFSET = 0.2;
        const doorColors = [0xff6644, 0xff5533, 0xff4422, 0xff3311];
        
        function createFoldedDoor(width, height, x, z, rot, colorIdx) {
            const group = new THREE.Group();
            const panelMat = new THREE.MeshStandardMaterial({ color: doorColors[colorIdx % 4], metalness: 0.65, roughness: 0.35 });
            const panel = new THREE.Mesh(new THREE.BoxGeometry(width, height, 0.08), panelMat);
            panel.castShadow = true;
            group.add(panel);
            const trimMat = new THREE.MeshStandardMaterial({ color: 0xdd8844 });
            for (let i = -height/2 + 0.8; i < height/2; i += 1.5) {
                const horzStiff = new THREE.Mesh(new THREE.BoxGeometry(width - 0.1, 0.06, 0.06), trimMat);
                horzStiff.position.set(0, i, 0.05);
                horzStiff.castShadow = true;
                group.add(horzStiff);
            }
            group.position.set(x, DOOR_Y, z);
            group.rotation.y = rot;
            scene.add(group);
            return group;
        }
        
        const doors = [];
        const southZ = -HALF_SIZE;
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, -HALF_SIZE, southZ, 0, 0), axis: 'x', open: -HALF_SIZE, closed: -HALF_SIZE + DOOR_WIDTH/2 });
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, -HALF_SIZE + STACK_OFFSET, southZ, 0, 1), axis: 'x', open: -HALF_SIZE + STACK_OFFSET, closed: -HALF_SIZE + DOOR_WIDTH*1.5 });
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, HALF_SIZE - STACK_OFFSET, southZ, 0, 2), axis: 'x', open: HALF_SIZE - STACK_OFFSET, closed: HALF_SIZE - DOOR_WIDTH*1.5 });
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, HALF_SIZE, southZ, 0, 3), axis: 'x', open: HALF_SIZE, closed: HALF_SIZE - DOOR_WIDTH/2 });
        
        const eastX = HALF_SIZE;
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, eastX, -HALF_SIZE, Math.PI/2, 0), axis: 'z', open: -HALF_SIZE, closed: -HALF_SIZE + DOOR_WIDTH/2 });
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, eastX, -HALF_SIZE + STACK_OFFSET, Math.PI/2, 1), axis: 'z', open: -HALF_SIZE + STACK_OFFSET, closed: -HALF_SIZE + DOOR_WIDTH*1.5 });
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, eastX, HALF_SIZE - STACK_OFFSET, Math.PI/2, 2), axis: 'z', open: HALF_SIZE - STACK_OFFSET, closed: HALF_SIZE - DOOR_WIDTH*1.5 });
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, eastX, HALF_SIZE, Math.PI/2, 3), axis: 'z', open: HALF_SIZE, closed: HALF_SIZE - DOOR_WIDTH/2 });
        
        const northZ = HALF_SIZE;
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, HALF_SIZE, northZ, Math.PI, 0), axis: 'x', open: HALF_SIZE, closed: HALF_SIZE - DOOR_WIDTH/2 });
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, HALF_SIZE - STACK_OFFSET, northZ, Math.PI, 1), axis: 'x', open: HALF_SIZE - STACK_OFFSET, closed: HALF_SIZE - DOOR_WIDTH*1.5 });
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, -HALF_SIZE + STACK_OFFSET, northZ, Math.PI, 2), axis: 'x', open: -HALF_SIZE + STACK_OFFSET, closed: -HALF_SIZE + DOOR_WIDTH*1.5 });
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, -HALF_SIZE, northZ, Math.PI, 3), axis: 'x', open: -HALF_SIZE, closed: -HALF_SIZE + DOOR_WIDTH/2 });
        
        const westX = -HALF_SIZE;
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, westX, HALF_SIZE, -Math.PI/2, 0), axis: 'z', open: HALF_SIZE, closed: HALF_SIZE - DOOR_WIDTH/2 });
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, westX, HALF_SIZE - STACK_OFFSET, -Math.PI/2, 1), axis: 'z', open: HALF_SIZE - STACK_OFFSET, closed: HALF_SIZE - DOOR_WIDTH*1.5 });
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, westX, -HALF_SIZE + STACK_OFFSET, -Math.PI/2, 2), axis: 'z', open: -HALF_SIZE + STACK_OFFSET, closed: -HALF_SIZE + DOOR_WIDTH*1.5 });
        doors.push({ obj: createFoldedDoor(DOOR_WIDTH, DOOR_HEIGHT, westX, -HALF_SIZE, -Math.PI/2, 3), axis: 'z', open: -HALF_SIZE, closed: -HALF_SIZE + DOOR_WIDTH/2 });
        
        let doorPos = 0;
        
        function updateDoors(factor) {
            doorPos = factor;
            doors.forEach(d => {
                if (d.axis === 'x') d.obj.position.x = d.open + (d.closed - d.open) * factor;
                else d.obj.position.z = d.open + (d.closed - d.open) * factor;
            });
            document.getElementById('sideFill').style.width = `${factor * 100}%`;
            document.getElementById('sidePercent').innerText = `${Math.floor(factor * 100)}%`;
            updateThreatDisplay();
            if (typeof updateStrikeButtonsState === 'function') updateStrikeButtonsState();
        }
        
        function animateDoors(target) {
            const start = doorPos;
            const startTime = performance.now();
            function step(now) {
                const t = Math.min(1, (now - startTime) / 500);
                updateDoors(start + (target - start) * t);
                if (t < 1) requestAnimationFrame(step);
            }
            requestAnimationFrame(step);
        }
        
        function updateThreatDisplay() {
            const threatLed = document.getElementById('threatLed');
            const threatText = document.getElementById('threatText');
            if (doorPos >= 0.95 && shutterExtension >= 0.95) {
                threatLed.style.background = "#3eff9e";
                threatText.innerHTML = "FULLY SEALED";
            } else if (shutterExtension >= 0.95) {
                threatLed.style.background = "#88ff88";
                threatText.innerHTML = "THREAT MODE (Shutters Extended)";
            } else if (doorPos >= 0.95) {
                threatLed.style.background = "#88ff88";
                threatText.innerHTML = "DOORS CLOSED";
            } else {
                threatLed.style.background = "#ffaa33";
                threatText.innerHTML = "NORMAL MODE (Doors Open)";
            }
        }
        
        // ==================== DRONE SYSTEM ====================
        let currentDrone = null;
        let currentDroneAnimationId = null;
        let currentDroneType = null;
        
        function updateStrikeButtonsState() {
            const hasDrone = currentDrone !== null;
            const isNormalDrone = currentDroneType === 'normal';
            const isThreatDrone = currentDroneType === 'threat';
            const doorsOpen = doorPos < 0.3;
            const shuttersExtended = shutterExtension >= 0.95;
            
            const normalEnabled = hasDrone && isNormalDrone && doorsOpen && !shuttersExtended;
            const threatEnabled = hasDrone && isThreatDrone && shuttersExtended && !doorsOpen;
            
            const normalButtons = ['strikeNormal1', 'strikeNormal2', 'strikeNormal3', 'strikeNormal4', 'strikeNormal5', 'strikeNormal6'];
            const threatButtons = ['strikeThreat1', 'strikeThreat2', 'strikeThreat3', 'strikeThreat4', 'strikeThreat5', 'strikeThreat6'];
            
            normalButtons.forEach(id => {
                const btn = document.getElementById(id);
                if (btn) {
                    btn.disabled = !normalEnabled;
                    btn.style.opacity = normalEnabled ? '1' : '0.5';
                    btn.style.cursor = normalEnabled ? 'pointer' : 'not-allowed';
                }
            });
            
            threatButtons.forEach(id => {
                const btn = document.getElementById(id);
                if (btn) {
                    btn.disabled = !threatEnabled;
                    btn.style.opacity = threatEnabled ? '1' : '0.5';
                    btn.style.cursor = threatEnabled ? 'pointer' : 'not-allowed';
                }
            });
            
            if (!hasDrone) {
                document.getElementById('droneStatus').innerHTML = '⚡ No drone active - Spawn a drone first';
            } else if (isNormalDrone) {
                if (doorsOpen && !shuttersExtended) {
                    document.getElementById('droneStatus').innerHTML = '🟢 NORMAL DRONE ACTIVE - Doors OPEN - Strikes READY';
                } else if (!doorsOpen) {
                    document.getElementById('droneStatus').innerHTML = '🟡 NORMAL DRONE ACTIVE - Doors CLOSED - Open doors to strike';
                } else if (shuttersExtended) {
                    document.getElementById('droneStatus').innerHTML = '🟡 NORMAL DRONE ACTIVE - Shutters EXTENDED - Retract shutters to strike';
                }
            } else if (isThreatDrone) {
                if (shuttersExtended && !doorsOpen) {
                    document.getElementById('droneStatus').innerHTML = '🔴 THREAT DRONE ACTIVE - Shutters EXTENDED - Strikes READY';
                } else if (!shuttersExtended) {
                    document.getElementById('droneStatus').innerHTML = '🟠 THREAT DRONE ACTIVE - Shutters RETRACTED - Extend shutters to strike';
                } else if (doorsOpen) {
                    document.getElementById('droneStatus').innerHTML = '🟠 THREAT DRONE ACTIVE - Doors OPEN - Close doors to strike';
                }
            }
        }
        
        function createDrone(type) {
            removeDrone();
            
            const drone = new THREE.Group();
            const bodyMat = new THREE.MeshStandardMaterial({ color: 0x334455, metalness: 0.72 });
            const body = new THREE.Mesh(new THREE.BoxGeometry(0.62, 0.26, 0.62), bodyMat);
            drone.add(body);
            
            for (let i = 0; i < 4; i++) {
                const a = (i / 4) * Math.PI * 2;
                const arm = new THREE.Mesh(new THREE.BoxGeometry(0.09, 0.06, 0.74), new THREE.MeshStandardMaterial({ color: 0x556677 }));
                arm.position.set(Math.cos(a) * 0.56, 0, Math.sin(a) * 0.56);
                arm.rotation.z = a;
                drone.add(arm);
                const rotor = new THREE.Mesh(new THREE.BoxGeometry(0.46, 0.04, 0.11), new THREE.MeshStandardMaterial({ color: 0xaaaabb }));
                rotor.position.set(Math.cos(a) * 0.88, 0.16, Math.sin(a) * 0.88);
                rotor.userData = { a: a };
                drone.add(rotor);
            }
            
            const lightColor = type === 'normal' ? 0x44ff88 : 0xff4444;
            const light = new THREE.Mesh(new THREE.SphereGeometry(0.12, 10, 10), new THREE.MeshStandardMaterial({ color: lightColor, emissive: lightColor, emissiveIntensity: 0.8 }));
            light.position.set(0, 0.2, 0.34);
            drone.add(light);
            
            scene.add(drone);
            currentDrone = drone;
            currentDroneType = type;
            
            const radius = type === 'normal' ? 16 : 14;
            const baseAlt = type === 'normal' ? 14 : 12;
            let angle = -Math.PI / 2;
            let t = 0;
            
            function fly() {
                if (!currentDrone) return;
                t += 0.008;
                angle = -Math.PI / 2 + t;
                const x = Math.cos(angle) * radius;
                const z = Math.sin(angle) * radius;
                const yOffset = Math.sin(t * 0.8) * 1.2;
                const y = baseAlt + yOffset;
                
                currentDrone.position.set(x, y, z);
                currentDrone.lookAt(0, 7, 0);
                currentDrone.children.forEach(c => { 
                    if (c.isMesh && c.userData.a !== undefined) c.rotation.x += 0.28; 
                });
                currentDroneAnimationId = requestAnimationFrame(fly);
            }
            fly();
            
            updateStrikeButtonsState();
        }
        
        function removeDrone() {
            if (currentDrone) {
                scene.remove(currentDrone);
                if (currentDroneAnimationId) cancelAnimationFrame(currentDroneAnimationId);
                currentDrone = null;
                currentDroneType = null;
                updateStrikeButtonsState();
            }
        }
        
        function droneStrike() {
            if (!currentDrone) {
                document.getElementById('impactMessage').innerHTML = "⚠️ No drone active! Spawn a drone first!";
                return;
            }
            
            const doorsOpen = doorPos < 0.3;
            const shuttersExtended = shutterExtension >= 0.95;
            
            if (currentDroneType === 'normal') {
                if (!doorsOpen) {
                    document.getElementById('impactMessage').innerHTML = "❌ NORMAL DRONE CANNOT STRIKE! Doors are closed! Open doors first!";
                    createExplosion(new THREE.Vector3(HALF_SIZE, 6, -HALF_SIZE), 0.4);
                    return;
                }
                if (shuttersExtended) {
                    document.getElementById('impactMessage').innerHTML = "❌ NORMAL DRONE CANNOT STRIKE! Shutters are extended! Retract shutters for normal mode!";
                    createExplosion(new THREE.Vector3(0, TOP_Y + 1, 0), 0.4);
                    return;
                }
                strikeAtPosition(new THREE.Vector3(1.6, 5.5, 1.6), 'tower', 0.7);
                document.getElementById('impactMessage').innerHTML = "🛸 NORMAL DRONE STRIKE! Minor damage to tower!";
            } else {
                if (!shuttersExtended) {
                    document.getElementById('impactMessage').innerHTML = "❌ THREAT DRONE CANNOT STRIKE! Shutters are not extended! Extend shutters first!";
                    createExplosion(new THREE.Vector3(0, TOP_Y + 1, 0), 0.4);
                    return;
                }
                if (doorsOpen) {
                    document.getElementById('impactMessage').innerHTML = "❌ THREAT DRONE CANNOT STRIKE! Doors are open! Close doors for threat mode!";
                    createExplosion(new THREE.Vector3(HALF_SIZE, 6, -HALF_SIZE), 0.4);
                    return;
                }
                strikeAtPosition(new THREE.Vector3(1.6, 5.5, 1.6), 'tower', 1.3);
                document.getElementById('impactMessage').innerHTML = "💀💀 THREAT DRONE IMPACT! MAJOR DAMAGE TO TOWER! 💀💀";
            }
        }
        
        // ==================== DRAMATIC FIRE & SMOKE EFFECTS ====================
        let activeFires = [];
        let activeSmokes = [];
        let fireIntervals = [];
        let smokeIntervals = [];
        
        function createDramaticFire(pos, intensity = 1.0) {
            const fireGroup = new THREE.Group();
            const coreFire = new THREE.Mesh(new THREE.SphereGeometry(0.55 * intensity, 20, 20), 
                new THREE.MeshStandardMaterial({ color: 0xff4400, emissive: 0xff2200, emissiveIntensity: 1.2 * intensity }));
            fireGroup.add(coreFire);
            
            const flameCount = Math.floor(80 * intensity);
            for (let i = 0; i < flameCount; i++) {
                const flame = new THREE.Mesh(new THREE.SphereGeometry(0.12 + Math.random() * 0.28, 8, 8), 
                    new THREE.MeshStandardMaterial({ color: 0xff6600, emissive: 0xff3300 }));
                flame.position.set((Math.random() - 0.5) * 1.5, Math.random() * 1.8, (Math.random() - 0.5) * 1.5);
                fireGroup.add(flame);
            }
            fireGroup.position.copy(pos);
            scene.add(fireGroup);
            activeFires.push(fireGroup);
            
            let step = 0;
            const fireInterval = setInterval(() => {
                if (!fireGroup.parent) { clearInterval(fireInterval); return; }
                step++;
                fireGroup.children.forEach(child => {
                    if (child.material) child.material.emissiveIntensity = Math.min(2.0, 0.8 + step * 0.06);
                });
                if (step > 50) clearInterval(fireInterval);
            }, 250);
            fireIntervals.push(fireInterval);
            
            setTimeout(() => {
                const idx = activeFires.indexOf(fireGroup);
                if (idx > -1) { scene.remove(fireGroup); activeFires.splice(idx, 1); }
            }, 8000);
        }
        
        function createMassiveSmoke(pos, intensity = 1.0) {
            const smokeGroup = new THREE.Group();
            const puffCount = Math.floor(60 * intensity);
            for (let i = 0; i < puffCount; i++) {
                const puff = new THREE.Mesh(new THREE.SphereGeometry(0.3 + Math.random() * 0.5, 10, 10), 
                    new THREE.MeshStandardMaterial({ color: 0x2a2a2a, transparent: true, opacity: 0.65 }));
                puff.position.set((Math.random() - 0.5) * 2.2, Math.random() * 2.0, (Math.random() - 0.5) * 2.2);
                smokeGroup.add(puff);
            }
            smokeGroup.position.copy(pos);
            scene.add(smokeGroup);
            activeSmokes.push(smokeGroup);
            
            let step = 0;
            const smokeInterval = setInterval(() => {
                if (!smokeGroup.parent) { clearInterval(smokeInterval); return; }
                step++;
                smokeGroup.children.forEach(puff => {
                    puff.scale.setScalar(1 + step * 0.045);
                    puff.material.opacity = Math.max(0.12, 0.65 - step * 0.015);
                    puff.position.y += 0.045;
                });
                if (step > 50) clearInterval(smokeInterval);
            }, 220);
            smokeIntervals.push(smokeInterval);
            
            setTimeout(() => {
                const idx = activeSmokes.indexOf(smokeGroup);
                if (idx > -1) { scene.remove(smokeGroup); activeSmokes.splice(idx, 1); }
            }, 7000);
        }
        
        function createExplosion(pos, intensity = 1.0) {
            const group = new THREE.Group();
            const particleCount = Math.floor(100 * intensity);
            for (let i = 0; i < particleCount; i++) {
                const p = new THREE.Mesh(new THREE.SphereGeometry(0.07 + Math.random() * 0.16, 6, 6), 
                    new THREE.MeshStandardMaterial({ color: 0xff5500, emissive: 0xff3300 }));
                p.position.copy(pos);
                p.userData = { v: new THREE.Vector3((Math.random() - 0.5) * 3.5, Math.random() * 3.5, (Math.random() - 0.5) * 3.5) };
                group.add(p);
            }
            const flash = new THREE.Mesh(new THREE.SphereGeometry(0.9 * intensity, 24, 24), 
                new THREE.MeshStandardMaterial({ color: 0xffaa44, emissive: 0xff6600, transparent: true }));
            flash.position.copy(pos);
            group.add(flash);
            scene.add(group);
            
            let start = performance.now();
            function anim() {
                const elapsed = (performance.now() - start) / 1000;
                if (elapsed > 1.0) { scene.remove(group); return; }
                const t = elapsed / 1.0;
                flash.material.opacity = 1 - t;
                flash.scale.setScalar(1 + t * 3.5);
                group.children.forEach(c => {
                    if (c.userData.v) {
                        c.position.x += c.userData.v.x * 0.09;
                        c.position.z += c.userData.v.z * 0.09;
                        c.position.y += c.userData.v.y * 0.09;
                        c.userData.v.y -= 0.12;
                    }
                });
                requestAnimationFrame(anim);
            }
            requestAnimationFrame(anim);
            camShake(intensity * 0.15);
        }
        
        function addDent(pos) {
            const dent = new THREE.Mesh(new THREE.SphereGeometry(0.4, 20, 20), new THREE.MeshStandardMaterial({ color: 0x8a6a4a, metalness: 0.1, roughness: 0.9 }));
            dent.position.copy(pos);
            dent.scale.set(0.7, 0.2, 0.7);
            scene.add(dent);
            setTimeout(() => scene.remove(dent), 10000);
        }
        
        function clearAllEffects() {
            activeFires.forEach(fire => scene.remove(fire));
            activeSmokes.forEach(smoke => scene.remove(smoke));
            fireIntervals.forEach(interval => clearInterval(interval));
            smokeIntervals.forEach(interval => clearInterval(interval));
            activeFires = [];
            activeSmokes = [];
            fireIntervals = [];
            smokeIntervals = [];
        }
        
        function camShake(intensity = 0.15) {
            const orig = camera.position.clone();
            let dur = 0;
            const interval = setInterval(() => {
                camera.position.x = orig.x + (Math.random() - 0.5) * intensity;
                camera.position.z = orig.z + (Math.random() - 0.5) * intensity;
                dur += 0.03;
                if (dur > 0.4) { clearInterval(interval); camera.position.copy(orig); }
            }, 25);
        }
        
        function strikeAtPosition(pos, type, intensity = 1.0) {
            createExplosion(pos, intensity);
            addDent(pos);
            
            if (type === 'tower') {
                createDramaticFire(pos, intensity);
                createMassiveSmoke(pos, intensity);
            }
        }
        
        // ==================== STRIKE DEFINITIONS ====================
        const normalStrikes = [
            { name: "Bottom Section", pos: new THREE.Vector3(1.2, 2.5, 1.2) },
            { name: "Lower Trays", pos: new THREE.Vector3(1.3, 4.0, 1.3) },
            { name: "Mid Trays", pos: new THREE.Vector3(1.4, 5.5, 1.4) },
            { name: "Upper Trays", pos: new THREE.Vector3(1.3, 7.0, 1.3) },
            { name: "Top Section", pos: new THREE.Vector3(1.2, 8.2, 1.2) },
            { name: "Overhead", pos: new THREE.Vector3(1.0, 9.2, 1.0) }
        ];
        
        const threatStrikes = [
            { name: "Top Dome", pos: new THREE.Vector3(0, TOP_Y + 0.5, 0) },
            { name: "East Platform", pos: new THREE.Vector3(HALF_SIZE + 0.3, 5.5, 0) },
            { name: "North Piping", pos: new THREE.Vector3(0, 6.5, HALF_SIZE + 0.3) },
            { name: "South Piping", pos: new THREE.Vector3(0, 4.5, -HALF_SIZE - 0.3) },
            { name: "West Platform", pos: new THREE.Vector3(-HALF_SIZE - 0.3, 7.5, 0) },
            { name: "Manway", pos: new THREE.Vector3(1.8, TOP_Y + 0.3, 1.8) }
        ];
        
        function executeNormalStrike(index) {
            if (!currentDrone || currentDroneType !== 'normal') {
                document.getElementById('impactMessage').innerHTML = "⚠️ Only NORMAL drone can perform normal strikes!";
                return;
            }
            if (doorPos >= 0.3) {
                document.getElementById('impactMessage').innerHTML = "❌ Doors are closed! Open doors for normal strikes!";
                createExplosion(new THREE.Vector3(HALF_SIZE, 6, -HALF_SIZE), 0.3);
                return;
            }
            if (shutterExtension >= 0.95) {
                document.getElementById('impactMessage').innerHTML = "❌ Shutters are extended! Normal drone cannot strike with shutters closed!";
                createExplosion(new THREE.Vector3(0, TOP_Y + 1, 0), 0.3);
                return;
            }
            
            const strike = normalStrikes[index];
            strikeAtPosition(strike.pos, 'tower', 0.8);
            document.getElementById('impactMessage').innerHTML = `🔥 NORMAL STRIKE: ${strike.name} - Fire damage!`;
        }
        
        function executeThreatStrike(index) {
            if (!currentDrone || currentDroneType !== 'threat') {
                document.getElementById('impactMessage').innerHTML = "⚠️ Only THREAT drone can perform threat strikes!";
                return;
            }
            if (shutterExtension < 0.95) {
                document.getElementById('impactMessage').innerHTML = "❌ Shutters are not extended! Extend shutters for threat strikes!";
                createExplosion(new THREE.Vector3(0, TOP_Y + 1, 0), 0.3);
                return;
            }
            if (doorPos < 0.3) {
                document.getElementById('impactMessage').innerHTML = "❌ Doors are open! Close doors for threat mode strikes!";
                createExplosion(new THREE.Vector3(HALF_SIZE, 6, -HALF_SIZE), 0.3);
                return;
            }
            
            const strike = threatStrikes[index];
            strikeAtPosition(strike.pos, 'threat', 1.0);
            document.getElementById('impactMessage').innerHTML = `💀 THREAT STRIKE: ${strike.name} - Structural damage!`;
        }
        
        function fullSeal() { animateDoors(1); animateShutters(1); setTimeout(() => updateStrikeButtonsState(), 600); }
        function resetAll() { animateDoors(0); animateShutters(0); removeDrone(); clearAllEffects(); setTimeout(() => updateStrikeButtonsState(), 600); }
        
        // UI Bindings
        document.getElementById('raiseSideBtn').onclick = () => { animateDoors(1); setTimeout(() => updateStrikeButtonsState(), 500); };
        document.getElementById('lowerSideBtn').onclick = () => { animateDoors(0); setTimeout(() => updateStrikeButtonsState(), 500); };
        document.getElementById('extendAllShuttersBtn').onclick = () => { animateShutters(1); setTimeout(() => updateStrikeButtonsState(), 600); };
        document.getElementById('retractAllShuttersBtn').onclick = () => { animateShutters(0); setTimeout(() => updateStrikeButtonsState(), 600); };
        document.getElementById('emergencyFullBtn').onclick = fullSeal;
        document.getElementById('resetShieldsBtn').onclick = () => { animateDoors(0); animateShutters(0); setTimeout(() => updateStrikeButtonsState(), 600); };
        document.getElementById('resetAllActionsBtn').onclick = resetAll;
        
        document.getElementById('spawnDroneNormalBtn').onclick = () => createDrone('normal');
        document.getElementById('spawnDroneThreatBtn').onclick = () => createDrone('threat');
        document.getElementById('removeDroneBtn').onclick = removeDrone;
        document.getElementById('droneStrikeBtn').onclick = droneStrike;
        
        // Normal strikes
        for (let i = 0; i < 6; i++) {
            document.getElementById(`strikeNormal${i+1}`).onclick = () => executeNormalStrike(i);
        }
        
        // Threat strikes
        for (let i = 0; i < 6; i++) {
            document.getElementById(`strikeThreat${i+1}`).onclick = () => executeThreatStrike(i);
        }
        
        // ==================== RESIZABLE PANEL ====================
        const panel = document.getElementById('movablePanel');
        const resizeHandle = document.getElementById('resizeHandle');
        let isResizing = false, startX, startY, startWidth, startHeight;
        
        resizeHandle.addEventListener('mousedown', (e) => {
            e.stopPropagation();
            isResizing = true;
            startX = e.clientX;
            startY = e.clientY;
            startWidth = panel.offsetWidth;
            startHeight = panel.offsetHeight;
            panel.style.cursor = 'nw-resize';
            e.preventDefault();
        });
        
        document.addEventListener('mousemove', (e) => {
            if (!isResizing) return;
            let newWidth = startWidth + (e.clientX - startX);
            let newHeight = startHeight + (e.clientY - startY);
            newWidth = Math.max(280, Math.min(600, newWidth));
            newHeight = Math.max(350, Math.min(800, newHeight));
            panel.style.width = newWidth + 'px';
            panel.style.height = newHeight + 'px';
        });
        
        document.addEventListener('mouseup', () => { isResizing = false; panel.style.cursor = 'grab'; });
        
        document.getElementById('resetPanelPos').onclick = () => {
            panel.style.left = 'auto';
            panel.style.right = '20px';
            panel.style.top = 'auto';
            panel.style.bottom = '20px';
            panel.style.width = '340px';
            panel.style.height = 'auto';
        };
        
        let drag = false, offX, offY;
        panel.addEventListener('mousedown', (e) => {
            if (e.target === resizeHandle || e.target.closest('button')) return;
            drag = true;
            const rect = panel.getBoundingClientRect();
            offX = e.clientX - rect.left;
            offY = e.clientY - rect.top;
            panel.style.cursor = 'grabbing';
        });
        
        document.addEventListener('mousemove', (e) => {
            if (!drag) return;
            let left = e.clientX - offX;
            let top = e.clientY - offY;
            left = Math.max(5, Math.min(window.innerWidth - panel.offsetWidth - 5, left));
            top = Math.max(5, Math.min(window.innerHeight - panel.offsetHeight - 5, top));
            panel.style.left = left + 'px';
            panel.style.top = top + 'px';
            panel.style.right = 'auto';
            panel.style.bottom = 'auto';
        });
        
        document.addEventListener('mouseup', () => { drag = false; panel.style.cursor = 'grab'; });
        
        // Initialize
        updateDoors(0);
        updateAllShutters(0);
        updateStrikeButtonsState();
        
        // Animation loop
        function animate() {
            controls.update();
            renderer.render(scene, camera);
            labelRenderer.render(scene, camera);
            requestAnimationFrame(animate);
        }
        animate();
        
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
            labelRenderer.setSize(window.innerWidth, window.innerHeight);
        });
        
        console.log('RAIED - Realistic CDU Tower with fractionating trays, platforms, piping, and industrial details');
    </script>
</body>
</html>