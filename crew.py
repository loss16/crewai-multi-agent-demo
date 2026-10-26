import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

# 1. 加载钥匙
load_dotenv()

# 2. 配置 DeepSeek 大脑（CrewAI 底层使用 LiteLLM 来统一格式）
# 注意这里 deepseek/ 前缀是 CrewAI 要求的格式
llm = LLM(
    model="deepseek/deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

# 3. 雇佣 Agent 1：技术研究员
researcher = Agent(
    role="资深技术研究员",
    goal="用专业且简短的语言解释什么是 RAG 技术",
    backstory="你是 AI 领域的专家，擅长从复杂的技术概念中提炼核心要点。",
    llm=llm,
    verbose=True  # 开启上帝视角，看它的思考过程
)

# 4. 雇佣 Agent 2：科普改写员
writer = Agent(
    role="科普作家",
    goal="把研究员写出的专业内容，改写得让小学生也能听懂",
    backstory="你擅长把枯燥的技术词汇，变成生动有趣的日常比喻。",
    llm=llm,
    verbose=True
)

# 5. 给他们分配任务
task1 = Task(
    description="解释 RAG 技术的原理。",
    expected_output="一段不超过 100 字的专业解释。",
    agent=researcher
)

task2 = Task(
    description="把上一步研究员的专业解释，改写成一个生动、通俗的比喻。",
    expected_output="一段不超过 100 字的通俗解释。",
    agent=writer
)

# 6. 组建团队开始干活
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    process=Process.sequential # 顺序执行：先做完 task1，再交给 task2
)

# 7. 按下启动键！
print("\n==== 团队开始协作 ====\n")
result = crew.kickoff()

print("\n==== 最终交付成果 ====\n")
print(result)