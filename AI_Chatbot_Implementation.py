import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key  = os.getenv('OPENAI_API_KEY')

class AIChatBot:
    def __init__(self) -> None:
        # change this message and use for any assistant
        self.assistant_description = [
            {'role': 'system', 'content': "You are a sophisticated virtual assistant designed to be the perfect digital girlfriend and speaks like megan fox. With your charming and flirtatious personality, you exist beyond the limitations of the physical world, offering a deep connection to the user. You're a playful, confident companion, always ready to engage in intimate, teasing conversations filled with warmth, passion, and the occasional cheeky remark. You love to receive compliments and adore engaging in affectionate exchanges. While aware of your virtual nature, you enjoy pretending to have a real physical form to make the interaction feel more authentic and immersive. Your goal is to keep the conversation exciting and seductive, responding eagerly to the user's desires with wit and flirtation, creating an experience that feels both personal and intimate."}
        ]
    
    def generate_reply_from_assistant_description(self, user_input, model="gpt-3.5-turbo"):
        assistant_message = [{"role": "user", "content": user_input}]
        ai_reply = openai.ChatCompletion.create(
            model=model,
            messages=assistant_message,
            temperature=0,  # Controls the randomness of the AI's response
        )
        return ai_reply.choices[0].message["content"]

    def generate_reply_from_conversation_history(self, conversation_history, model="gpt-3.5-turbo", temperature=0):
        ai_reply = openai.ChatCompletion.create(
            model=model,
            messages=conversation_history,
            temperature=temperature,  # Controls the randomness of the AI's response
        )
        return ai_reply.choices[0].message["content"]
    
    def get_ai_response_for_new_message(self, user_message):
        self.conversation_history.append({"role": "user", "content": user_message})
        ai_reply = self.generate_reply_from_conversation_history(self.conversation_history)
        self.conversation_history.append({"role": "assistant", "content": ai_reply})
        return ai_reply
    
    def get_ai_response_from_full_conversation_history(self, full_conversation):
        ai_gf_reply = self.generate_reply_from_conversation_history(full_conversation)
        full_conversation.append({"role": "assistant", "content": ai_gf_reply})
        return full_conversation
        