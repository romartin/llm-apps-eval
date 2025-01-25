import os
import sys
from locust import FastHttpUser, task, between, run_single_user

API_TOKEN = os.getenv("API_TOKEN")


class ChatbotUser(FastHttpUser):
    connection_timeout = 60.0
    network_timeout = 60.0
    max_retries = 3
    wait_time = between(1, 10)

    # Chatbot Response content example:
    # {
    #    "conversation_id": "...",
    #    "response": "Hello! I'm Ansible Lightspeed, your virtual assistant for all things Ansible. How can I assist you today?",
    #    "referenced_documents": [],
    #    "truncated": false
    # }
    #

    queries = [
        "What is new in AAP 2.5?",
        "How can I migrate from AAP 2.4 to 2.5?",
        "What is Platform Gateway?",
        "Write a sample inventry file.",
        "What is Ansible Lightspeed?",
    ]

    @task
    def chat_completion(self):
        conversation_id = None
        for query in self.queries:
            response = self.call_chat_completion(query, conversation_id)
            if response.status_code > 0:
                response_json = response.json()
                conversation_id = response_json["conversation_id"]

    def call_chat_completion(self, query, conversation_id):
        headers = {
            "Content-Type": "application/json",
            'Accept': 'application/json',
        }

        if API_TOKEN is not None:
            headers["Authorization"] = f"Bearer {API_TOKEN}"

        payload = {
            "model": "granite3-8b",
            "provider": "my_rhoai_g3",
            "query": query,
        }

        if conversation_id is not None:
            payload["conversation_id"] = conversation_id

        with self.client.post("", json=payload, headers=headers, debug_stream=sys.stderr) as response:
            return response

# if launched directly, e.g. "python3 debugging.py", not "locust -f debugging.py"
if __name__ == "__main__":
    run_single_user(ChatbotUser)