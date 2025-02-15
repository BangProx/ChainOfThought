import openai
from typing import List, Dict, Any


class ChainOfThought:
    def __init__(self, api_key: int):
        """
        Initiate Class for Chain of Thought reasoning

        Args:
            api_key (str): OpenAI API KEY
        """
        self.client = openai.OpenAI(api_key=api_key)

    def create_cot_prompt(self, question: str) -> str:
        """
        Generate Chain of Thought Prompt

        Args:
            question (str): User's Question

        Returns:
            str: CoT Prompt
        """
        template = f"""Please Think Step by Step for input question
        Input Question : {question}
        Lets Think Step By Step :
        """

        return template

    def get_response(self, prompt: str) -> str:
        """
        Get Repsonse from LLM

        Args :
            prompt (str): CoT Prompt

        Returns :
            str : Response of LLM
        """

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in solving problems logically. Please explain each step clearly.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content

    def solve(self, question: str) -> Dict[str, Any]:
        """
        Solves the problem using the Chain of Thought approach.

        Args:
            question (str): The problem or question to be solved

        Returns:
            Dict[str, Any]: The result including step-by-step reasoning and the final answer
        """
        prompt = self.create_cot_prompt(question)
        response = self.get_response(prompt)

        # Split the response into steps
        steps = response.split("\n")

        return {
            "question": question,
            "reasoning_steps": steps,
            "final_answer": steps[-1] if steps else "Unable to find an answer.",
        }
