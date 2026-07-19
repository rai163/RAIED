<!DOCTYPE html>
<html>
<head>
    <title>RAIED Trapezoidal Shutters</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background: black;
        }
        #sim {
            display: block;
            margin: 0 auto;
            background: black;
        }
        #controls {
            position: absolute;
            top: 10px;
            left: 10px;
            color: white;
            font-family: Arial, sans-serif;
            font-size: 20px;
        }
    </style>
</head>
<body>

<div id="controls">
    SPACE: Deploy &nbsp;&nbsp; R: Retract &nbsp;&nbsp; ESC: Reset
</div>

<canvas id="sim" width="1280" height="720"></canvas>

<script>
const canvas = document.getElementById("sim");
const ctx = canvas.getContext("2d");

let tankImg = new Image();
tankImg.src = "tank.png";

const buryDepth = 80;
const riseSpeed = 4;

// Build a shutter as a rigid quadrilateral that slides along its own normal
function makeQuadShutter(name, tl, tr, br, bl) {
    const midTop = {
        x: (tl.x + tr.x) / 2,
        y: (tl.y + tr.y) / 2
    };
    const midBottom = {
        x: (bl.x + br.x) / 2,
        y: (bl.y + br.y) / 2
    };

    const dx = midBottom.x - midTop.x;
    const dy = midBottom.y - midTop.y;
    const len = Math.sqrt(dx*dx + dy*dy) || 1;
    const nx = dx / len;
    const ny = dy / len;

    return {
        name,
        tl, tr, br, bl,
        midTop,
        nx, ny,
        offset: buryDepth,
        buriedOffset: buryDepth,
        targetOffset: 0
    };
}

// Middle shutter (rectangle, unchanged)
const middleTL = { x: 508, y: 270 };
const middleTR = { x: 765, y: 270 };
const middleBL = { x: 508, y: 390 };
const middleBR = { x: 765, y: 390 };

// LEFT SHUTTER (updated)
const leftTL =