let expression = '';
const display = document.getElementById('display');

function updateDisplay() {
    if (expression === '') {
        display.textContent = '0';
    } else {
        let shown = expression
            .replace(/\//g, '÷')
            .replace(/\*/g, '×')
            .replace(/-/g, '−');
        display.textContent = shown;
    }
}

function addChar(char) {
    expression += char;
    updateDisplay();
}

function clearAll() {
    expression = '';
    updateDisplay();
}

function percent() {
    try {
        let result = eval(expression) / 100;
        expression = result.toString();
        updateDisplay();
    } catch (e) {
        // ignore
    }
}

function calculate() {
    try {
        let result = eval(expression);
        if (result === Infinity || result === -Infinity) {
            expression = 'Error';
        } else if (Number.isInteger(result)) {
            expression = result.toString();
        } else {
            expression = parseFloat(result.toFixed(8)).toString();
        }
    } catch (e) {
        expression = 'Error';
    }
    updateDisplay();
    if (expression === 'Error') {
        expression = '';
    }
}

document.addEventListener('keydown', (e) => {
    if (e.key >= '0' && e.key <= '9') addChar(e.key);
    else if (e.key === '+' || e.key === '-' || e.key === '*' || e.key === '/') addChar(e.key);
    else if (e.key === '.') addChar(e.key);
    else if (e.key === 'Enter' || e.key === '=') calculate();
    else if (e.key === 'Backspace') { expression = expression.slice(0, -1); updateDisplay(); }
    else if (e.key === 'Escape') clearAll();
    else if (e.key === '%') percent();
});
