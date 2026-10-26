# 基于 CrewAI 的多智能体（Multi-Agent）协作原型

## 项目简介
本项目基于 CrewAI 框架，构建了由“资深技术研究员”与“科普作家”两个角色组成的智能体流水线。验证了多 Agent 在复杂内容生成与风格转换场景下的协作能力。

## 技术栈
- 框架：CrewAI (基于 LiteLLM)
- 大模型：DeepSeek API
- 核心机制：Process.sequential (顺序执行流)

## 核心亮点
1. **角色化定义（Role-playing）**：通过定义不同的 Role、Goal 和 Backstory，让大模型在特定领域内发挥最大效能。
2. **任务解耦（Task Chaining）**：将“专业解释”与“通俗改写”拆分为两个独立的 Task，由不同 Agent 负责，实现业务流的流水线作业。
3. **异构模型集成**：通过 `deepseek/deepseek-chat` 格式成功接入国产大模型，打通了多 Agent 协作的底层链路。

## 运行方式
1. 安装依赖：`pip install crewai crewai-tools python-dotenv`
2. 配置 `.env` 文件（包含 `DEEPSEEK_API_KEY`）。
3. 运行 `crew.py`。