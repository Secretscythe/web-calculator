# 🧮 Advanced Scientific, Graphing & Calculus Suite

A modern calculator suite featuring a Desmos-style graphing engine, calculus tools (tangent lines, derivatives, definite integrals), dynamic parameter sliders, a universal unit converter, a scientific calculator, and a native Python desktop GUI.

---

## ✨ Features

### 1. 📈 Desmos-Style Graphing & Calculus Engine
- **Multi-Function Plotting:** Plot multiple functions simultaneously ($f_1(x), f_2(x), \dots$) with distinct colors.
- **Dynamic Parameter Sliders:** Use variables $a, b, c$ in equations (e.g. $a \cdot x^2 + b \cdot x + c$, $a \cdot \sin(b \cdot x)$) with live animated play/pause sliders.
- **Tangent Line & Derivative Tracker ($\frac{dy}{dx}$):** Draggable tangent point $P(x_0, f(x_0))$ with live numerical derivative computation, slope readout, and tangent line equation.
- **Definite Integral & Area Shading ($\int_a^b f(x)\,dx$):** Real-time area under the curve visualization with numerical integration.
- **Interactive Coordinate Plane:** Smooth pan, scroll zoom, live coordinate tracking, and origin centering.

### 2. 🔬 Scientific Calculator
- **Powers & Roots:** $x^y, x^2, x^3, \sqrt{x}, \sqrt[3]{x}, \sqrt[y]{x}$
- **Trigonometry & Inverses:** $\sin, \cos, \tan, \sin^{-1}, \cos^{-1}, \tan^{-1}$ with DEG / RAD angle modes.
- **Logarithms & Constants:** $\ln, \log_{10}, \log_2, e^x, \pi, e$
- **History Tape:** Interactive calculation history log.

### 3. 🔄 Universal Unit Converter
- **9 Measurement Categories:** Length, Mass/Weight, Temperature, Area, Volume, Speed, Time, Data Storage, Energy & Power.
- **Real-Time Bidirectional:** Instant calculation as you type with unit swapping and quick comparison tables.

### 4. 🖥️ Native Desktop GUI & CLI
- **Desktop GUI:** Built with Python `tkinter` (`gui_calculator.py`).
- **CLI REPL:** Terminal evaluator with expression support (`calculator.py`).

---

## 🚀 How to Run

### Web Application
Open `web_calculator.html` in any browser, or run the local Python server:
```bash
python3 server.py
```
Then visit: [http://localhost:8000/web_calculator.html](http://localhost:8000/web_calculator.html)

### Native Desktop GUI
```bash
python3 gui_calculator.py
```

### CLI Evaluator & Tests
```bash
python3 calculator.py
python3 -m unittest test_calculator.py
```
