import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()

jobs = [
    """"We use an internal CRM and want to give our management team a clear, AI-powered view of the business. We need a developer who can quickly build a working prototype of an AI agent that processes CRM records and turns them into KPIs, available both on the web and on mobile.                                                                                                                                                                                                        
                                                                                                                                                                                                        
This is a small, one-time task, ideal for someone who builds prototypes fast with Claude Code or Codex.                                                                                                                                                                                                        
                                                                                                                                                                                                        
What we need                                                                                                                                                                                                        
                                                                                                                                                                                                        
1) AI agent (core of the project)                                                                                                                                                                                                        
- Connect to our CRM through its API, read records (deals, contacts, tasks, activities) and process them on a schedule.                                                                                                                                                                                                        
- The agent should follow a decision loop: fetch data, analyze, decide which metrics or alerts matter, generate KPIs and short summaries, save the results.                                                                                                                                                                                                        
- AI model integration with an LLM (OpenAI, Claude or similar). Simple machine learning for forecasting or anomaly detection is a plus.                                                                                                                                                                                                        
- Expose the results through a small REST backend (API development), so the web and mobile apps can use the same data.                                                                                                                                                                                                        
2) Web dashboard (Next.js)                                                                                                                                                                                                        
- A responsive web application with charts, KPI cards and filters (by period, manager, pipeline stage).                                                                                                                                                                                                        
- Front-end development with HTML5, CSS and Tailwind CSS. Clean, simple UI; no heavy design work needed.                                                                                                                                                                                                        
- Our current CRM admin panel is built with Vue.js. Some existing widgets may need to be reused or rebuilt, so Vue experience is a plus.                                                                                                                                                                                                        
3) Mobile app (React Native, preferred)                                                                                                                                                                                                        
- An AI mobile app for management: the same KPIs, push alerts for important changes, and a simple AI chatbot to ask questions like “How did sales do this week compared to last week?”                                                                                                                                                                                                        
- We haven’t fully decided on the stack, but we’re leaning toward React Native. If you’d suggest something else, explain why.                                                                                                                                                                                                        
                                                                                                                                                                                                        
In your proposal, please describe:                                                                                                                                                                                                        
                                                                                                                                                                                                        
1) How you would implement the agent’s decision loop. Give a concrete example. For instance: the agent detects that deals stuck in “Negotiation” have grown 30% week over week, decides it’s a risk, creates an alert and adds a short explanation to the dashboard.                                                                                                                                                                                                        
2) Which tools you’d use for AI agent development (LangChain, LangGraph, OpenAI Assistants, a custom loop, etc.) and why.                                                                                                                                                                                                        
3) Whether we can later add a RAG system to analyze our database, with examples of what it could do, such as:                                                                                                                                                                                                        
- “Why did we lose most deals in Q3?”, answered from deal notes and call logs                                                                                                                                                                                                        
- Finding similar past clients or deals for a new lead                                                                                                                                                                                                        
- Summarizing a client’s full history before a meeting                                                                                                                                                                                                        
- Answering internal questions about processes, based on our documents and CRM data                                                                                                                                                                                                        
                                                                                                                                                                                                        
Ideal candidate                                                                                                                                                                                                        
                                                                                                                                                                                                        
1) Full-stack development experience (Node.js/Python backend, Next.js, React Native)                                                                                                                                                                                                        
2) Hands-on experience with AI agents, automation and LLM API integration                                                                                                                                                                                                        
3) Uses Claude Code or Codex daily and can deliver a working prototype fast                                                                                                                                                                                                        
4) Can explain technical decisions in simple terms to non-technical managers                                                                                                                                                                                                        """,
    """pFull stack development
Posted 40 minutes ago
Worldwide

Summary
UI/UX Designer & Developer - Lovable + Replit - Immediate Start

We're building several ventures and need a hands-on designer/developer who can start immediately.

Caxton Wealth is one example: caxtonwealth.com. We want distinctive, polished websites and product interfaces, not generic templates.

You should have:
- Strong UI, UX, visual design and development skills
- Hands-on experience with Lovable, Replit and no-code platforms
- Familiarity with Dribbble and similar design-reference sites, with the ability to turn references into original, working pages
- Excellent typography, layout, interaction and responsive design skills
- Attention to detail, clear communication and the ability to work independently

To apply, please send 
- two or three relevant live examples, 
- your best redesign concept for the Caxton Wealth homepage (not the whole site): caxtonwealth.com.

The purpose is to see your design capability: your visual judgement, creativity, typography, layout and attention to detail.

Keep our existing video and written content. Show how you would improve their presentation, visual hierarchy, spacing and interactions.

You're welcome to use Dribbble, similar reference sites and your preferred design tools. The final site will use a no-code platform such as Lovable, so your concept should be realistic to build and maintain there.

 A desktop mockup is enough; no development or live-site access is required. We'll use it only to assess your approach, not publish it or use it commercially without a separate agreement""",
    """Full-Stack AI Developer

We are hiring a part-time full-stack developer to build and maintain AI features in an existing product. This is an ongoing role.

What you will do
- Build AI features across the stack: UI, API, and model integration.
- Connect LLMs or agents to real product flows (prompts, tools, structured output, and error handling).
- Ship small, working changes and keep the codebase easy to run and edit.
- Fix bugs in the AI path and explain what changed in plain language.

Scope
- One product, incremental delivery. No large rewrites unless we agree on them first.
- Out of scope: a full-time commitment, open-ended research, or unrelated feature work.

You should have
- Full-stack experience (a modern frontend plus a backend API).
- Hands-on work shipping LLM or AI-agent features, not only prototypes.
- Comfort reading an existing codebase and making small, safe changes.
- Clear written updates on what you built and what is left.

To apply
Send:
1. One full-stack AI feature you shipped (short description or link).
2. How you would approach AI work on a product that already exists.
3. Your rate and when you can start.""",
]

system_prompt = (
    "Extract job details. Reply ONLY with JSON with keys: "
    "title (string), skills (list of strings), budget_usd (number or null), "
    "deadline_days (number or null), "
    # TODO: add the good_fit key here (true if the job uses React, Next.js or Node)
    "good_fit (true if the job uses react  , next js , or node)"
)


for job in jobs:
    
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "Extract job details. Reply ONLY with JSON with keys: "
                                        "title (string), skills (list of strings), budget_usd (number or null), "
                                        "deadline_days (number or null).good_fit (boolean: true if the job is full-stack JavaScript work (React/Next.js/Node) "
                                        "OR involves building AI/LLM features, else false), "
                                        "reason (string: one sentence explaining good_fit)"
                                        "skills (list of strings: ONLY skills explicitly written in the post, never guess),"},
            {"role": "user", "content": job},
        ],
        response_format={"type": "json_object"},
    )

    text = response.choices[0].message.content
  


    try:
        data = json.loads(text)
        print(data["title"], "|", data["good_fit"], "|", data["reason"])
      
    except json.JSONDecodeError :
        print("Bad json")