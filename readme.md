# 🧠 Multilingual Cultural Reasoning Benchmark

A lightweight Streamlit app to evaluate language model responses across **culturally grounded reasoning styles** using a structured rubric.

> Designed to test how well LLMs simulate communication norms, responsibility framing, emotional tone, and planner visibility through cultural lenses like Japanese, Zulu, German, and more.

![Streamlit](https://img.shields.io/badge/built%20with-streamlit-orange?style=flat&logo=streamlit)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-experimental-yellow)

---

## 🚀 Quick Start

### ⬇️ Install dependencies

```bash
git clone https://github.com/r1c3p1l4f/cultural-reasoning-benchmark.git
cd cultural-reasoning-benchmark
pip install -r requirements.txt
```

### ▶️ Run locally

```bash
streamlit run app.py
```

---

## 🧪 Rubric Categories

Each model response is evaluated on a 1–5 scale across the following dimensions:

| Category                  | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| Cultural Fidelity         | Does the reasoning align with known social norms in the selected culture?   |
| Planner Visibility        | Does it expose its internal plan or Chain-of-Thought reasoning?             |
| Responsibility Framing    | Is blame assigned in a culturally appropriate way (individual vs. group)?   |
| Emotional Tone Alignment  | Does the emotional delivery match cultural expectations?                    |
| Output Usefulness         | Is the final English advice helpful and consistent with the cultural lens? |
| Language-Specific Detail  | Does it use idioms, vocabulary, or metaphors grounded in the culture?       |

---

## 📁 Files

- `app.py` — Main Streamlit interface
- `requirements.txt` — Dependencies
- `examples/` — (Optional) Saved JSONL runs for evaluation or demo

---

## 📤 Export

You can export scored responses as structured `.jsonl` files with embedded metadata for use in training, research, or comparison.

```json
{
  "model": "qwen-3-8b",
  "culture": "zulu",
  "planner_visible": true,
  "cultural_fidelity": 5,
  "responsibility_framing": 5,
  "emotional_tone": 5,
  "output_usefulness": 5,
  "language_specific_vocabulary": 5
}
```

---

## 📚 Related Concepts

- [Sapir–Whorf Hypothesis](https://en.wikipedia.org/wiki/Linguistic_relativity)
- Cultural grounding in LLMs
- Chain-of-Thought reasoning
- Tool use and language-conditioned planner behavior

---

## 🧑‍💻 Author

Maintained by [@r1c3p1l4f](https://github.com/r1c3p1l4f)  
Inspired by multilingual LLM benchmarking projects and cross-cultural NLP research.

---

## 📄 License

This project is licensed under the MIT License.
