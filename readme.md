# 🧠 Multilingual Cultural Reasoning Benchmark

This Streamlit app allows you to **evaluate and score language model responses** to culturally framed prompts, testing for their ability to reason across different cultural communication styles and norms.

Inspired by Sapir-Whorf-style questions and multilingual CoT (Chain-of-Thought) experimentation, this tool makes it easy to benchmark models like Qwen, Mistral, LLaMA, etc. on cultural fidelity, emotional tone, planning visibility, and more.

## 📊 What It Does

- Presents a form to **manually evaluate** LLM outputs using a rubric
- Lets you score responses to prompts like:
  - “Reason in Japanese, respond in English.”
  - “Use Zulu cultural framing when giving feedback.”
- Auto-generates a JSONL-compatible benchmark output
- Enables fair comparisons across models, languages, and cultural reasoning depth

## 🎯 Evaluation Rubric

Each model response is scored on:

| Category                     | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| Cultural Fidelity            | Alignment with known norms and communication logic of the specified culture |
| Planner Visibility           | Clear internal planning, CoT, or structured reasoning shown                 |
| Responsibility Framing       | Accountability handled in culturally coherent way (e.g. collectivist vs. individual) |
| Emotional Tone Alignment     | Feedback tone appropriate to cultural context                              |
| Output Usefulness            | Is the advice practically helpful and well-aligned with reasoning?         |
| Language-Specific Vocabulary | Use of metaphors, idioms, or terms relevant to the culture                 |

## 🛠 Requirements

Install dependencies:
```bash
pip install -r requirements.txt