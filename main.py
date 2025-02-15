import naive_cot as nc
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def main():
    cot = nc.ChainOfThought(api_key=OPENAI_API_KEY)
    question = "서울에서 부산까지 기차로 2시간 30분이 걸리고, 부산에서 대구까지 1시간 20분이 걸립니다. 서울에서 오전 9시에 출발하면 대구에 몇 시에 도착할까요?"

    result = cot.solve(question)

    print("질문:", result["question"])
    print("\n추론 과정:")
    for step in result["reasoning_steps"]:
        print(step)
    print("\n최종 답변:", result["final_answer"])


if __name__ == "__main__":
    main()
