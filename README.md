# Narratex - AI-Assisted Audio Exercises for Patients with ADHD and Brain Injuries

## Overview

This project aims to develop an **AI-powered audio delivery system** tailored to support **Brainwave-R cognitive assessments**, especially for patients suffering from **ADHD**, **brain injuries**, and other **attention-related disorders**. The tool combines **text-to-speech (TTS)** technology with **facial emotion recognition** to provide a comprehensive, inclusive, and independent cognitive testing experience.

## Problem Statement

Patients with ADHD, depression, anxiety, or brain injuries often struggle with traditional text-based cognitive assessments like Brainwave-R due to:

* Reading fatigue
* Attention lapses
* Language barriers
* Unavailability of support
* Privacy concerns

These issues hinder independent participation in cognitive rehabilitation exercises.

---

## Objectives

1. **Eliminate dependence** on others for reading test modules.
2. Build a **cognitive-aware TTS engine** that adapts speed, tone, and emphasis.
3. Develop a **standardized auditory module** for inclusive and precise test delivery.

---

## Proposed Solution

An **AI-powered Text-to-Audio System** that:

* Converts Brainwave-R content into natural-sounding speech.
* Supports dynamic pacing and tone adjustment.
* Includes a **facial emotion recognition module** for real-time user state monitoring.
* Offers both **doctor and patient portals** for interaction and analysis.

---

## Literature Review & Gaps Identified

* **Current cognitive training apps** do not cater to text comprehension challenges.
* Lack of **technology integration** in Brainwave-R.
* Absence of **adaptive TTS** and **standardized auditory testing frameworks**.

---

## Technical Architecture

### Technologies Used

#### Audio Generation

* `gTTS`, `pydub`, `playsound`
* `pytesseract`, `pdf2image`, `PIL`, `re`, `numpy`

#### Facial Recognition

* `dlib`, `OpenCV`, `scikit-learn`, `pandas`, `matplotlib`

#### Backend

* Python, Flask, Cloudinary (for audio hosting)

#### Frontend

* React.js, Typescript, JavaScript

---

## Key Features

* **PDF-to-Audio Conversion** with cognitive-aware TTS
* **Emotion Monitoring** using facial recognition
* **Interactive Patient Interface** and **Doctor Dashboard**
* **Real-time Feedback** and test performance summary

---

## Evaluation Metrics

| Metric                        | Value | Purpose                               |
| ----------------------------- | ----- | ------------------------------------- |
| Words Per Minute (WPM)        | 20.77 | Measures speech pace                  |
| Word Error Rate (WER)         | 1%    | Checks accuracy of TTS                |
| Intersection over Union (IoU) | 0.893 | Accuracy of facial landmark detection |
| Mean Squared Error (MSE)      | -     | Used for facial model evaluation      |

---

## Project Outcomes

* Independent auditory-based test module
* Real-time facial emotion analysis
* Reduced dependency on external support
* Enhanced inclusivity in cognitive assessments

---

## Future Enhancements

* Integration with deep learning emotion detection
* Personalized user feedback and adaptive pacing
* Wider module coverage beyond Brainwave-R

---

## References

1. [https://doi.org/10.1016/j.ijhcs.2024.103402](https://doi.org/10.1016/j.ijhcs.2024.103402)
2. [https://doi.org/10.1093/jamiaopen/ooz011](https://doi.org/10.1093/jamiaopen/ooz011)
3. [https://link.springer.com/article/10.1007/s12559-023-10153-4](https://link.springer.com/article/10.1007/s12559-023-10153-4)
4. [PMC: Cognitive Retraining](https://pmc.ncbi.nlm.nih.gov/articles/PMC3927143/)
5. [Cambridge CNS Spectrums Article](https://www.cambridge.org/core/journals/cns-spectrums/article/attentional-problems-occur-across-multiple-psychiatric-disorders-and-are-not-specific-for-adhd/EFA24E1CB1C6A779220A123288BDB329)
6. [Cognitive Retraining via ResearchGate](https://www.researchgate.net/publication/349971658_Cognitive_Retraining_attention_Module_among_Students_with_Internet_Addiction)

---
