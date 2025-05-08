const spaceBackground = document.getElementById('space-background');

// Create shooting stars
function createShootingStars() {
    for (let i = 0; i < 5; i++) {
        const shootingStar = document.createElement('div');
        shootingStar.classList.add('shooting-star');
        shootingStar.style.top = `${Math.random() * 100}%`;
        shootingStar.style.left = `${Math.random() * 100}%`;
        shootingStar.style.animationDelay = `${Math.random() * 10}s`;
        spaceBackground.appendChild(shootingStar);
    }
}

createStars();
createShootingStars();

document.getElementById('generateBtn').addEventListener('click', function () {
    const inputText = document.getElementById('inputText').value.trim();
    if (inputText) {
        // 发送请求到 Flask 后端
        fetch('/generate_reference', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({inputText: inputText}),
        })
            .then(response => response.json())
            .then(data => {
                const harvardReference = data.harvardReference;

                // Hide input container and show result container
                document.querySelector('.container').classList.add('hidden');
                document.querySelector('.result-container').classList.remove('hidden');

                // Display generated reference
                document.getElementById('outputText').innerHTML = harvardReference;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    } else {
        alert('Please paste some text to generate a reference.');
    }
});


document.getElementById('copyBtn').addEventListener('click', function () {
    const outputText = document.getElementById('outputText').innerText;
    navigator.clipboard.writeText(outputText).then(() => {
        // 复制成功后更改按钮字样
        const copyButton = document.getElementById('copyBtn');
        copyButton.textContent = 'Copied!'; // 更改按钮文字
        setTimeout(() => {
            copyButton.textContent = 'Copy'; // 1 秒后恢复原文字
        }, 1000);
    }).catch((err) => {
        console.error('Failed to copy text: ', err);
    });
});

document.getElementById('backBtn').addEventListener('click', function () {
    // Hide result container and show input container
    document.querySelector('.result-container').classList.add('hidden');
    document.querySelector('.container').classList.remove('hidden');

    // Clear input text
    document.getElementById('inputText').value = '';
});

document.getElementById('guideBtn').addEventListener('click', function () {
    window.location.href = "/doc";
});

// 生成星星和流星动画
function createStars() {
    const spaceBackground = document.getElementById('space-background');
    const starCount = 100; // 星星数量
    const shootingStarCount = 3; // 流星数量

    // 生成星星
    for (let i = 0; i < starCount; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.top = `${Math.random() * 100}%`;
        star.style.left = `${Math.random() * 100}%`;
        star.style.animationDuration = `${Math.random() * 2 + 1}s`; // 随机动画时长
        spaceBackground.appendChild(star);
    }

    // 生成流星
    for (let i = 0; i < shootingStarCount; i++) {
        const shootingStar = document.createElement('div');
        shootingStar.className = 'shooting-star';
        shootingStar.style.top = `${Math.random() * 20}%`; // 流星从顶部 20% 以内开始
        shootingStar.style.left = `${Math.random() * 100}%`;
        shootingStar.style.animationDuration = `${Math.random() * 2 + 1}s`; // 随机动画时长
        spaceBackground.appendChild(shootingStar);
    }
}


// 初始化
document.addEventListener('DOMContentLoaded', createStars);

function returnToHome() {
    window.location.href = '/'; // 跳转到主页
}