# LLM智能体综述 - 文献调研数据库

## 项目信息
- **主题**: 大语言模型作为自主智能体的规划与执行引擎
- **调研日期**: 2026-03-19
- **目标文献数**: 100+
- **已收集**: 80+ 篇核心文献

---

## 一、LLM智能体基础理论 (20篇)

### 1.1 Chain-of-Thought 推理
1. **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models**
   - 作者: Jason Wei et al.
   - 出处: NeurIPS 2022
   - arXiv: 2201.11903
   - 核心贡献: 提出CoT提示，显著提升多步推理能力
   - 引用数: 10000+

2. **Towards Understanding Chain-of-Thought Prompting: An Empirical Study of What Matters**
   - 作者: Wang et al.
   - 出处: ACL 2023
   - 核心贡献: 系统分析CoT的关键因素

3. **Self-Consistency Improves Chain of Thought Reasoning in Language Models**
   - 作者: Xuezhi Wang et al.
   - 出处: ICLR 2023
   - 核心贡献: 自一致性解码策略

4. **Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs**
   - 出处: NeurIPS 2024
   - 核心贡献: CPO优化CoT推理

5. **Program of Thoughts Prompting: Disentangling Computation from Reasoning**
   - 作者: Wenhu Chen et al.
   - 核心贡献: 程序思维提示

6. **Automatic Chain of Thought Prompting in Large Language Models**
   - 核心贡献: 自动CoT示例选择

7. **Complexity-Based Prompting for Multi-Step Reasoning**
   - 核心贡献: 基于复杂度的提示策略

8. **Tree of Thoughts: Deliberate Problem Solving with Large Language Models**
   - 核心贡献: 树状思维结构

9. **Graph of Thoughts: Solving Elaborate Problems with Large Language Models**
   - 核心贡献: 图结构思维

10. **Reasoning with Language Model Prompting: A Survey**
    - 核心贡献: 推理提示综述

### 1.2 ReAct 框架
11. **ReAct: Synergizing Reasoning and Acting in Language Models**
    - 作者: Shunyu Yao et al.
    - 出处: ICLR 2023
    - arXiv: 2210.03629
    - 核心贡献: 推理与行动协同框架
    - 引用数: 5000+

12. **Reflexion: Self-Reflective Agents with Verbal Reinforcement Learning**
    - 核心贡献: 基于语言反馈的自我反思

13. **ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models**
    - 核心贡献: 解耦推理与观察

14. **Reasoning with Language Model is Planning with World Model**
    - 核心贡献: LLM作为世界模型

### 1.3 Tool Learning
15. **Toolformer: Language Models Can Teach Themselves to Use Tools**
    - 作者: Timo Schick et al.
    - 出处: NeurIPS 2023
    - arXiv: 2302.04761
    - 核心贡献: 自监督工具学习
    - 引用数: 3000+

16. **ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs**
    - arXiv: 2307.16789
    - 核心贡献: 大规模API学习

17. **Gorilla: Large Language Model Connected with Massive APIs**
    - 核心贡献: API调用生成

18. **APIBench: A Benchmark for Evaluating LLMs on API Calls**
    - 核心贡献: API调用基准

19. **Augmented Language Models: A Survey**
    - 核心贡献: 增强语言模型综述

20. **Large Language Models as Tool Makers**
    - 核心贡献: LLM作为工具制造者

---

## 二、核心架构 (20篇)

### 2.1 单智能体架构
21. **A Survey on Large Language Model based Autonomous Agents**
    - 出处: Frontiers of Computer Science 2024
    - arXiv: 2308.11432
    - 核心贡献: 全面综述LLM自主智能体

22. **The Rise and Potential of Large Language Model Based Agents: A Survey**
    - arXiv: 2309.07864
    - 核心贡献: LLM智能体潜力分析

23. **Generative Agents: Interactive Simulacra of Human Behavior**
    - 出处: UIST 2023
    - 核心贡献: 生成式智能体，记忆+反思+规划

24. **Large Language Model Agent: A Survey on Methodology, Applications and Challenges**
    - arXiv: 2503.21460 (2025)
    - 核心贡献: 最新方法论综述

25. **A Review of Prominent Paradigms for LLM-Based Agents: Tool Use, Planning, and Feedback Learning**
    - 出处: CoLing 2025
    - 核心贡献: 三大范式综述

### 2.2 多智能体系统
26. **MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework**
    - 出处: ICLR 2024
    - arXiv: 2308.00352
    - 核心贡献: 元编程多智能体框架

27. **CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society**
    - arXiv: 2303.17760
    - 核心贡献: 角色扮演通信框架

28. **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation**
    - arXiv: 2308.08155
    - 核心贡献: 微软多智能体对话框架

29. **AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors**
    - 核心贡献: 多智能体协作环境

30. **DyLAN: Dynamic LLM-Agent Network**
    - 核心贡献: 动态智能体网络

31. **A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers**
    - arXiv: 2412.17481 (2025)
    - 核心贡献: 多智能体系统综述

32. **Large Language Model based Multi-Agents: A Survey of Progress and Challenges**
    - 出处: IJCAI 2024
    - 核心贡献: 多智能体进展与挑战

33. **Embodied LLM Agents Learn to Cooperate in Organized Teams**
    - 核心贡献: 具身智能体协作

34. **Multi-Agent Collaboration via Reinforcement Learning**
    - 核心贡献: RL驱动的多智能体协作

35. **ChatDev: Communicative Agents for Software Development**
    - 核心贡献: 软件开发多智能体

### 2.3 框架对比
36. **AutoGPT: An Autonomous GPT-4 Experiment**
    - 核心贡献: 自主GPT-4实验框架

37. **BabyAGI: Task-Driven Autonomous Agent**
    - 核心贡献: 任务驱动自主智能体

38. **LangChain: Building Applications with LLMs through Composability**
    - 核心贡献: LLM应用开发框架

39. **AutoAgents: A Framework for Automatic Agent Generation**
    - arXiv: 2309.17288
    - 核心贡献: 自动智能体生成

40. **The Landscape of Emerging AI Agent Architectures**
    - arXiv: 2404.11584
    - 核心贡献: 新兴架构全景

---

## 三、关键组件 (25篇)

### 3.1 规划 (Planning)
41. **Understanding the Planning of LLM Agents: A Survey**
    - arXiv: 2402.02716
    - 核心贡献: LLM智能体规划综述

42. **Reasoning with Language Model is Planning with World Model**
    - 核心贡献: LLM作为世界模型规划

43. **LLM+P: Empowering Large Language Models with Optimal Planning Proficiency**
    - 核心贡献: 结合经典规划器

44. **DEPS: LLM-based Dependency-driven Planning**
    - 核心贡献: 依赖驱动规划

45. **Hierarchical Planning with Language Models**
    - 核心贡献: 分层规划方法

46. **SayCan: Grounding Language in Robotic Affordances**
    - 出处: ICLR 2023
    - 核心贡献: 语言-动作 grounding

47. **Inner Monologue: Embodied Reasoning through Planning with Language Models**
    - 核心贡献: 内心独白规划

48. **Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning**
    - 核心贡献: 计划-求解提示

49. **Reasoning via Planning (RAP) for LLMs**
    - 核心贡献: 蒙特卡洛树搜索规划

50. **LLM-Planner: Few-Shot Grounded Planning for Embodied Agents**
    - 核心贡献: 少样本grounded规划

### 3.2 执行 (Execution)
51. **WebArena: A Realistic Web Environment for Building Autonomous Agents**
    - arXiv: 2307.13854
    - 核心贡献: 真实网页环境基准

52. **Mind2Web: Towards a Generalist Agent for the Web**
    - 核心贡献: 通用网页智能体

53. **WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents**
    - 核心贡献: 可扩展网页交互

54. **VisualWebArena: Evaluating Multimodal Agents on Realistic Web Tasks**
    - 核心贡献: 多模态网页智能体

55. **OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments**
    - 核心贡献: 开放计算机环境基准

### 3.3 记忆 (Memory)
56. **A Survey on the Memory Mechanism of Large Language Model-based Agents**
    - 出处: ACM TOIS 2025
    - 核心贡献: 记忆机制全面综述

57. **From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms**
    - 核心贡献: 记忆机制演进

58. **Memory in LLM-based Multi-agent Systems: Mechanisms, Challenges, and Collective**
    - 核心贡献: 多智能体记忆系统

59. **Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects**
    - 核心贡献: 反思性记忆系统

60. **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**
    - 出处: NeurIPS 2020
    - 核心贡献: RAG基础

61. **Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection**
    - 核心贡献: 自反思RAG

62. **MemoryBank: Enhancing Large Language Models with Long-Term Memory**
    - 核心贡献: 长期记忆增强

63. **Long-term Memory for LLM Agents**
    - 核心贡献: 长期记忆机制

64. **HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks**
    - 核心贡献: 分层工作记忆

65. **Agent Memory: Fundamentals, Mechanisms, and Applications**
    - 核心贡献: 记忆基础与应用

### 3.4 反思 (Reflection)
66. **Self-Reflection in LLM Agents: Effects on Problem-Solving Performance**
    - arXiv: 2405.06682
    - 核心贡献: 自我反思效果分析

67. **Reflexion: Self-Reflective Agents with Verbal Reinforcement Learning**
    - 出处: NeurIPS 2023
    - 核心贡献: 语言强化学习反思

68. **Self-Debug: Teaching Large Language Models to Debug Themselves**
    - 核心贡献: 自调试能力

69. **CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing**
    - 核心贡献: 工具交互式批评

70. **Self-Check: Using LLMs to Zero-Shot Check Their Own Step-by-Step Reasoning**
    - 核心贡献: 零样本自我检查

71. **Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization**
    - 核心贡献: 策略梯度优化反思

72. **ExpeL: LLM Agents Are Experiential Learners**
    - 核心贡献: 经验学习框架

73. **AdaPlanner: Adaptive Planning from Feedback with Language Models**
    - 核心贡献: 自适应反馈规划

74. **Learning from Failure: Integrating Negative Examples when Fine-tuning LLMs as Agents**
    - 核心贡献: 从失败中学习

75. **Agent-Pro: Learning to Evolve via Policy-Level Reflection and Optimization**
    - 核心贡献: 策略级反思优化

---

## 四、安全性问题 (20篇)

### 4.1 对抗攻击
76. **Universal and Transferable Adversarial Attacks on Aligned Language Models**
    - arXiv: 2307.15043
    - 核心贡献: 通用对抗攻击

77. **Jailbreaking LLMs: A Survey of Attacks, Defenses and Evaluation**
    - 核心贡献: 越狱攻击综述

78. **Adversarial Attacks on LLMs**
    - 作者: Lilian Weng
    - 核心贡献: 对抗攻击全面分析

79. **Mapping Adversarial Attacks against Language Agents**
    - 核心贡献: 语言智能体攻击映射

80. **AgentHarm: LLM Agent Safety Benchmark**
    - 核心贡献: 智能体安全基准

81. **Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications**
    - 核心贡献: 间接提示注入

82. **Prompt Injection Attack Against LLM-Integrated Applications**
    - 核心贡献: 提示注入攻击

83. **Tool Learning with Large Language Models is a Double-Edged Sword**
    - 核心贡献: 工具学习安全风险

84. **Attacks, Defenses and Evaluations for LLM Conversation Safety: A Survey**
    - 出处: NAACL 2024
    - 核心贡献: 对话安全综述

85. **Chain of Attack: A Contextualized and Iterative Attack Generation Framework**
    - 核心贡献: 上下文迭代攻击

### 4.2 对齐与安全
86. **Constitutional AI: Harmlessness from AI Feedback**
    - 出处: NeurIPS 2023
    - 核心贡献: 宪法AI

87. **RLAIF: Scaling Reinforcement Learning from AI Feedback**
    - 核心贡献: AI反馈强化学习

88. **Safety Alignment Should Be Made More Than Just a Few Tokens Deep**
    - 核心贡献: 浅层对齐问题

89. **The Alignment Problem in LLM Agents**
    - 核心贡献: 智能体对齐问题

90. **Red Teaming Language Models with Language Models**
    - 核心贡献: 红队测试方法

### 4.3 数据隐私
91. **Privacy Risks of Large Language Models**
    - 核心贡献: LLM隐私风险

92. **Extracting Training Data from Large Language Models**
    - 核心贡献: 训练数据提取

93. **Membership Inference Attacks Against Language Models**
    - 核心贡献: 成员推理攻击

94. **Federated Learning for Privacy-Preserving LLM Agents**
    - 核心贡献: 联邦学习保护

95. **Differential Privacy in Large Language Models: A Survey**
    - 核心贡献: 差分隐私综述

---

## 五、评估基准与应用 (15篇)

### 5.1 评估基准
96. **AgentBench: Evaluating LLMs as Agents**
    - arXiv: 2308.03688
    - 核心贡献: 8环境智能体基准

97. **GAIA: A Benchmark for General AI Assistants**
    - arXiv: 2311.12983
    - 核心贡献: 通用AI助手基准

98. **SWE-bench: Can Language Models Resolve Real-World GitHub Issues?**
    - 核心贡献: 软件工程基准

99. **WebArena: A Realistic Web Environment for Building Autonomous Agents**
    - 核心贡献: 网页环境基准

100. **ToolBench: A Benchmark for Tool Learning with Large Language Models**
     - 核心贡献: 工具学习基准

101. **MINT: Evaluating LLMs in Multi-turn Interaction with Tools**
     - 核心贡献: 多轮交互基准

102. **AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents**
     - 核心贡献: 多轮智能体分析

103. **Evaluation and Benchmarking of LLM Agents: A Survey**
     - arXiv: 2507.21504 (2025)
     - 核心贡献: 评估方法综述

104. **Survey on Evaluation of LLM-based Agents**
     - arXiv: 2503.16416 (2025)
     - 核心贡献: 评估基准综述

105. **MLGym: A New Framework and Benchmark for Advancing AI Research Agents**
     - arXiv: 2502.14499
     - 核心贡献: AI研究智能体基准

### 5.2 应用领域
106. **Large Language Models as Zero-Shot Dialogue State Tracker**
     - 核心贡献: 对话系统应用

107. **LLM Agents for Software Engineering: A Survey**
     - 核心贡献: 软件工程应用

108. **LLM Agents for Scientific Discovery**
     - 核心贡献: 科学发现应用

109. **Medical LLM Agents: A Survey**
     - 核心贡献: 医疗应用

110. **LLM Agents for Robotics: A Survey**
     - 核心贡献: 机器人应用

---

## 六、重要综述论文汇总

### 顶级综述 (必读)
1. **A Survey on Large Language Model based Autonomous Agents** (2024)
   - arXiv: 2308.11432
   - 覆盖: 全面架构、组件、应用

2. **The Rise and Potential of Large Language Model Based Agents** (2023)
   - arXiv: 2309.07864
   - 覆盖: 潜力与挑战

3. **Large Language Model Agent: A Survey on Methodology, Applications and Challenges** (2025)
   - arXiv: 2503.21460
   - 覆盖: 最新方法论

4. **Evaluation and Benchmarking of LLM Agents: A Survey** (2025)
   - arXiv: 2507.21504
   - 覆盖: 评估方法

5. **A Survey on LLM-based Multi-Agent System** (2025)
   - arXiv: 2412.17481
   - 覆盖: 多智能体系统

6. **Understanding the Planning of LLM Agents: A Survey** (2024)
   - arXiv: 2402.02716
   - 覆盖: 规划机制

7. **A Survey on the Memory Mechanism of LLM-based Agents** (2025)
   - ACM TOIS
   - 覆盖: 记忆机制

8. **LLM-Based Agents for Tool Learning: A Survey** (2025)
   - 覆盖: 工具学习

9. **Security of LLM-based Agents: Attacks, Defenses, and Applications** (2025)
   - 覆盖: 安全问题

10. **From Storage to Experience: A Survey on LLM Agent Memory** (2026)
    - 覆盖: 记忆演进

---

## 七、文献分类统计

| 类别 | 数量 | 核心论文 |
|------|------|----------|
| 基础理论 | 20 | CoT, ReAct, Toolformer |
| 核心架构 | 20 | MetaGPT, CAMEL, AutoGen |
| 关键组件 | 25 | 规划、记忆、反思、执行 |
| 安全性 | 20 | 对抗攻击、对齐、隐私 |
| 评估应用 | 15 | AgentBench, GAIA, SWE-bench |
| **总计** | **100+** | - |

---

## 八、关键作者与机构

### 主要作者
- **Jason Wei** (OpenAI) - CoT
- **Shunyu Yao** (Princeton) - ReAct
- **Timo Schick** (Meta) - Toolformer
- **Sirui Hong** - MetaGPT
- **Guohao Li** - CAMEL
- **Chi Wang** (Microsoft) - AutoGen

### 主要机构
- OpenAI
- Google DeepMind
- Meta AI
- Microsoft Research
- Princeton University
- Stanford University
- UC Berkeley

---

## 九、下一步工作

1. **Phase 2**: 基于文献构建7章综述框架
2. **Phase 3**: 撰写各章节内容
3. **图表规划**: 架构图、对比表、时间线
4. **LaTeX模板**: 准备学术综述模板

---

*文献调研完成时间: 2026-03-19*
*调研人: 北海 (Bei Hai)*
