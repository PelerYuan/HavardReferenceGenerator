document.getElementById('generateBtn').addEventListener('click', function () {
    const inputText = document.getElementById('inputText').value.trim();
    if (inputText) {
        // Simulate generating Harvard reference (replace with actual logic)
        const harvardReference = `Author, A. (Year). Title of the work. Journal Name, Volume(Issue), Page Range.`;

        // Hide input container and show result container
        document.querySelector('.container').classList.add('hidden');
        document.querySelector('.result-container').classList.remove('hidden');

        // Display generated reference
        document.getElementById('outputText').textContent = harvardReference;
    } else {
        alert('Please paste some text to generate a reference.');
    }
});

document.getElementById('copyBtn').addEventListener('click', function () {
    const outputText = document.getElementById('outputText').textContent;
    navigator.clipboard.writeText(outputText).then(() => {
        alert('Reference copied to clipboard!');
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
    alert('Usage Guide:\n1. Paste your text into the input box.\n2. Click "Generate Reference" to create a Harvard-style reference.\n3. Copy the result to your clipboard.');
});
