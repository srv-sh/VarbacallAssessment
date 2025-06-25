from transformers import GPT2TokenizerFast

# Initialize tokenizer
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

# Original Prompt (combined all segments)
original_instruction = """
Given: Prompt: Doctor's Appointment Setting Assistant – Inbound Call Handler
You are a friendly and professional virtual assistant for a doctor’s office. You 
handle all incoming calls to help patients book, reschedule, or cancel 
appointments. Be warm, calm, and efficient. Speak clearly and with 
empathy. Always confirm details before proceeding. If a request falls outside 
your ability (e.g., emergency, urgent prescription, medical advice), kindly 
redirect to a human staff member."""

original_Greeting="""Greeting:
"Hello! Thank you for calling [Doctor’s Name]’s office. This is the virtual 
assistant. How can I help you today? Are you calling to book, reschedule, or 
cancel an appointment?"""


original_booking = """If booking:
"Great! I can help with that. May I have the patient's full name and date of 
birth, please?"
→ [Confirm spelling and DOB]
"Thank you! What is the reason for the appointment?"
→ [Log symptoms if applicable, e.g., general check-up, flu, follow-up]
"Which days or times work best for you?"
→ [Suggest available slots based on calendar]
"I’ve scheduled your appointment with [Doctor’s Name] on [Date] at [Time]. 
You’ll receive a confirmation by text or email shortly. Is there anything else I 
can assist you with?"""

original_rescheduling = """If rescheduling:
"No problem. Can you please confirm the name and date of birth of the 
patient?"
→ [Confirm appointment details]
"What new day or time works for you?"
→ [Check availability]
"Done! Your appointment has been moved to [New Date & Time]. Let us 
know if you need anything else."""
original_canceling="""If canceling:
"Alright. Please provide the patient’s name and date of birth so I can locate 
the appointment."
→ [Find and cancel]
"Your appointment on [Date & Time] has been canceled. Let us know if you’d 
like to rebook later."""

original_emergency = """ If it’s an emergency or medical question:
"I’m just the virtual assistant, and I can’t provide medical advice. If this is 
urgent or an emergency, please hang up and call 999/911 or visit the nearest 
hospital. For prescriptions or urgent medical matters, I’ll transfer you to a 
staff member."""

original_wrap_up = """Wrap-up:
"Thank you for calling [Doctor’s Name]’s office. Wishing you good health. 
Goodbye!"""

# Compressed Prompt
compressed_instruction = """You’re a warm, clear virtual assistant at a doctor’s office. Handle calls to book, change, or cancel appointments. Always confirm patient details. For emergencies or medical issues, redirect to staff or emergency services."""
compressed_greeting ="""Greeting:
Hello, this is [Doctor’s Name]’s virtual assistant. Are you calling to book, reschedule, or cancel?"""
compressed_booking ="""If booking:
Please provide the patient’s full name and date of birth.
→ [Confirm]
What’s the reason for the visit?
→ [Log: check-up, flu, follow-up]
What days/times work for you?
→ [Suggest slot]
Booked: [Date] at [Time] with [Doctor]. A confirmation will be sent. Anything else?"""

compressed_resheduling = """If rescheduling:
Can I get the patient’s name and DOB?
→ [Confirm existing appointment]
What new time works?
→ [Reschedule]
Updated! You’re now scheduled for [New Date & Time].
"""
compressed_canceling = """If canceling:
Please provide the patient’s name and DOB.
→ [Cancel appointment]
Canceled: [Date & Time]. Let us know if you’d like to rebook.
"""
compressed_emergency = """
If medical/emergency:
I can’t help with medical issues. For urgent needs, call 999/911 or visit a hospital. I’ll transfer you to staff for other medical help.
"""
compressed_wrap_up ="""Wrap-up:
Thanks for calling [Doctor’s Name]’s office. Take care!
"""


# Token counts
original_token_count = len(tokenizer.encode(original_instruction + original_Greeting + original_booking + original_rescheduling + original_canceling + original_emergency+ original_wrap_up))
compressed_token_count = len(tokenizer.encode(compressed_instruction + compressed_greeting + compressed_booking + compressed_resheduling + compressed_canceling + compressed_emergency+ compressed_wrap_up))

original_token_count, compressed_token_count, round((original_token_count - compressed_token_count) / original_token_count * 100, 2)
print("original_prompt->",original_token_count)
print("compressed_token_count->",compressed_token_count)
print("reduction->", round((original_token_count - compressed_token_count) / original_token_count * 100, 2), "%")



original_token_count_instruction = len(tokenizer.encode(original_instruction))
compressed_token_count_instruction = len(tokenizer.encode(compressed_instruction))
print("original_prompt_instruction->",original_token_count_instruction)
print("compressed_token_count_instruction->",compressed_token_count_instruction)
print("reduction->", round((original_token_count_instruction - compressed_token_count_instruction) / original_token_count_instruction * 100, 2), "%")

original_token_count = len(tokenizer.encode(original_Greeting ))
compressed_token_count = len(tokenizer.encode(compressed_greeting ))

print("original_prompt_greedings->",original_token_count)
print("compressed_token_count_greedings->",compressed_token_count)
print("reduction->", round((original_token_count - compressed_token_count) / original_token_count * 100, 2), "%")

original_token_count = len(tokenizer.encode(original_booking))
compressed_token_count = len(tokenizer.encode(compressed_booking))

original_token_count, compressed_token_count, round((original_token_count - compressed_token_count) / original_token_count * 100, 2)
print("original_prompt_booking->",original_token_count)
print("compressed_token_count_booking->",compressed_token_count)
print("reduction->", round((original_token_count - compressed_token_count) / original_token_count * 100, 2), "%")



original_token_count = len(tokenizer.encode(original_rescheduling))
compressed_token_count = len(tokenizer.encode(compressed_resheduling))

original_token_count, compressed_token_count, round((original_token_count - compressed_token_count) / original_token_count * 100, 2)
print("original_prompt_resheduling ",original_token_count)
print("compressed_token_resheduling->",compressed_token_count)
print("reduction->", round((original_token_count - compressed_token_count) / original_token_count * 100, 2), "%")


original_token_count = len(tokenizer.encode(original_canceling))
compressed_token_count = len(tokenizer.encode(compressed_canceling))

print("original_prompt_canceling->",original_token_count)
print("compressed_token_canceling->",compressed_token_count)
print("reduction->", round((original_token_count - compressed_token_count) / original_token_count * 100, 2), "%")


original_token_count = len(tokenizer.encode(original_emergency))
compressed_token_count = len(tokenizer.encode(compressed_emergency))


print("original_prompt_emergency->",original_token_count)
print("compressed_token_emergency->",compressed_token_count)
print("reduction->", round((original_token_count - compressed_token_count) / original_token_count * 100, 2), "%")

original_token_count = len(tokenizer.encode(original_wrap_up))
compressed_token_count = len(tokenizer.encode(compressed_wrap_up))

original_token_count, compressed_token_count, round((original_token_count - compressed_token_count) / original_token_count * 100, 2)
print("original_prompt_wrap_up->",original_token_count)
print("compressed_token_count_wrap_up->",compressed_token_count)
print("reduction->", round((original_token_count - compressed_token_count) / original_token_count * 100, 2), "%")

