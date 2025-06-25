# 🛠️ Part 3: Backend Reliability – Call Session Recovery Architecture

##  Scenario Overview

> A **patient calls** to **book a flu shot**.  
> The **call drops mid-way**.  
> The **patient calls back later**.  
> The **system resumes the conversation from where it left off**.

This architecture ensures a seamless experience by maintaining call context and resuming incomplete sessions without frustrating repetition for the caller.

---

##  Solution Architecture

![Solution Architecture Diagram](../diagrams/solution_architecture.png)  
*Figure 1: Persistent Session Recovery System*

###  Initial Call Flow (Flu Shot Booking)

1. **Incoming Call Received**  
   - Handled by **Voice Gateway**

2. **Routing**  
   - Call forwarded to **Call Router**

3. **Speech Transcription**  
   - **STT Engine** (e.g., Whisper) transcribes voice to text

4. **Session Check (Session Manager)**  
   - Session lookup in Redis  
   - If session **does not exist** → create a **new session**

5. **New Session Created**  
   - Stored in **Redis** with:
     - `Session ID` (UUID)
     - `Call State`: e.g., `booking_flu_shot`
     - Partial booking information
     - GPT dialog history (partial context)

6. **Conversation Progresses**  
   - **GPT Service** manages dialog and updates context  
   - Patient is asked for appointment date, time, etc.

7. **Call Drop Occurs**  
   - Session marked **incomplete** but retained in Redis

---

##  Call Recovery Flow (Patient Calls Back)

1. **Patient Reconnects**  
   - Voice Gateway receives second call  
   - Routed through Call Router to **Session Manager**

2. **Session Check**  
   - Redis queried for existing session  
   - If session **exists** → retrieve session context

3. **Session Restoration**  
   - Restore:
     - Booking state
     - GPT dialog history
     - Any provided patient information

4. **GPT Resumes Dialog Seamlessly**  
   - Example: _“Welcome back! You were booking a flu shot. We were about to select a date…”_

5. **Booking Completed**  
   - Final appointment details confirmed

6. **CRM Update**  
   - Sync with backend:
     - Appointment scheduled
     - Patient information logged
     - Full call history updated

7. **Confirmation Sent**  
   - **TTS Service** delivers confirmation response to caller

8. **Session Finalization**  
   - Marked as **complete**
   - Session data is deleted from Redis

---

##  End-to-End Flow Diagram

![Flow Diagram](../diagrams/flow_architecture.png)  
*Figure 2: Detailed Call Session Flow*

---

##  Phase 1: Initial Call (Before Drop)

| **Step**                  | **Details**                                                                 |
|---------------------------|------------------------------------------------------------------------------|
| Patient calls             | Dials clinic to book flu shot                                               |
| Voice Gateway             | Accepts and routes the call                                                 |
| Call Router               | Forwards to **Session Manager**                                             |
| Session Manager           | Creates new `Session ID` (UUID), stores in **Redis**                        |
| Booking initiated         | GPT assistant begins booking process, e.g., _“What date would you prefer?”_ |
| Session partially filled  | Captures phone number, intent stage, conversation context                   |
| Call drop                 | Session remains cached in Redis, marked **incomplete**                      |

---

##  Phase 2: Call Recovery (Patient Calls Back)

| **Step**                  | **Details**                                                                 |
|---------------------------|------------------------------------------------------------------------------|
| Caller ID matched         | Based on same phone number or session fingerprint                           |
| Redis queried             | Looks for active sessions                                                   |
| Session found             | Restores GPT context + previous dialog state                                |
| GPT resumes seamlessly    | _“Welcome back! You were booking a flu shot for next week…”_                |
| Booking completed         | Appointment time confirmed                                                  |
| CRM updated               | Syncs data across patient records and logs                                  |
| TTS response delivered    | Voice confirmation to patient                                               |
| Session closed            | Session deleted from Redis                                                  |

---

##  Key Components

| **Component**    | **Responsibility**                                                                 |
|------------------|-------------------------------------------------------------------------------------|
| Voice Gateway    | Ingests and routes all inbound calls                                                |
| Call Router      | Distributes call to appropriate service                                             |
| Session Manager  | Maintains session state, handles recovery, manages Redis integration                |
| Redis Cache      | Stores in-progress session data (TTL managed)                                       |
| GPT Service      | Maintains natural dialog, handles context continuation                              |
| CRM System       | Syncs appointments and patient interaction history                                  |
| STT / TTS        | Converts voice to text (Whisper / Deepgram) and back to voice for confirmation      |

---

 **Conclusion:**  
This system provides a **robust, context-aware** call experience. Patients can continue their booking journey **without repeating themselves**, and staff systems remain **synchronized**, enhancing operational efficiency and caller satisfaction.
