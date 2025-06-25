## Part 1: Prompt Optimization & Reliability  
### 2. Robust Prompt Logic (Adversarial Inputs)

#### Goal:
Handle adversarial or unclear speech-to-text (STT) outputs to avoid LLM hallucination or misinterpretation.

---

### Scenario 1: Vague Intent
**STT Output:**  
> "Umm... I wanted to do something with my... uh... appointment maybe next week or cancel it?"

**Risk:**  
Ambiguous intent — could mean booking, rescheduling, or canceling.

**Robust Handling Logic:**

→ If the intent is unclear, prompt clarification using a forced-choice:
"I'm here to help! Just to confirm — are you looking to book, reschedule, or cancel an appointment?"


**LLM Prompt Strategy:**
- Use a classification layer before the assistant prompt (intent router).
- If confidence < threshold (e.g., 70%), trigger fallback clarification prompt.

---

### Scenario 2: STT Hallucination or Garbled Input  
**STT Output:**  
> "Yeah I want to boop canthursday namesome flu maybe next week."

**Risk:**  
STT distortion causes garbled, hallucinated words (“boop canthursday”).

**Robust Handling Logic:**

→ Detect low semantic coherence or unknown entities.
"Sorry, I didn't catch that. Could you please repeat your request — are you trying to book, reschedule, or cancel an appointment?"


**LLM Prompt Strategy:**
- Include logic for repetition/confirmation fallback after low semantic confidence.
- Use minimal context prompting like:


---

### Summary: How Hallucination is Prevented

| Problem                  | Strategy                             | Result                             |
|--------------------------|--------------------------------------|------------------------------------|
| Ambiguous intent         | Forced-choice clarification          | Avoids false assumption            |
| Garbled STT input        | Detect noise, ask to repeat          | Prevents LLM from hallucinating    |
| STT errors from accents  | NLU + fallback confirmation prompts  | Ensures intent validation          |

---

**Fallback Example:**
> "Just to confirm, are you calling to book, reschedule, or cancel?"

This ensures **LLM reliability** even in real-world noisy, low-quality, or vague inputs.
