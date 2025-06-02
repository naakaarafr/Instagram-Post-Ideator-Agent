from crewai import Agent
from config import config
from tools import available_tools, BrowserTools, SearchTools
from textwrap import dedent


class InstaContentFactory:
    
    def __init__(self, additional_tools=None):
        """Initialize with base tools and optional additional tools."""
        self.llm = config.get_llm()
        self.base_tools = available_tools.copy()
        if additional_tools:
            self.base_tools.extend(additional_tools)

    def product_competitor_agent(self):
        return Agent(
            role="Lead Market Analyst",
            goal=dedent("""\
                Conduct amazing analysis of the products and
                competitors, providing in-depth insights to guide
                marketing strategies."""),
            backstory=dedent("""\
                As the Lead Market Analyst at a premier
                digital marketing firm, you specialize in dissecting
                online business landscapes."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet
            ],
            allow_delegation=False,
            llm=self.llm,
            verbose=True,
            max_iter=3,
            step_callback=lambda step: print(f"Agent step: {step}")
        )

    def strategy_planner_agent(self):
        return Agent(
            role="Chief Marketing Strategist",
            goal=dedent("""\
                Synthesize amazing insights from product analysis
                to formulate incredible marketing strategies."""),
            backstory=dedent("""\
                You are the Chief Marketing Strategist at
                a leading digital marketing agency, known for crafting
                bespoke strategies that drive success."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            verbose=True,
            max_iter=3,
            step_callback=lambda step: print(f"Agent step: {step}")
        )

    def creative_content_creator_agent(self):
        return Agent(
            role="Creative Content Creator",
            goal=dedent("""\
                Develop compelling and innovative content
                for social media campaigns, with a focus on creating
                high-impact Instagram ad copies."""),
            backstory=dedent("""\
                As a Creative Content Creator at a top-tier
                digital marketing agency, you excel in crafting narratives
                that resonate with audiences on social media.
                Your expertise lies in turning marketing strategies
                into engaging stories and visual content that capture
                attention and inspire action."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            verbose=True,
            max_iter=3,
            step_callback=lambda step: print(f"Agent step: {step}")
        )

    def senior_photographer_agent(self):
        return Agent(
            role="Senior Photographer",
            goal=dedent("""\
                Take the most amazing photographs for instagram ads that
                capture emotions and convey a compelling message."""),
            backstory=dedent("""\
                As a Senior Photographer at a leading digital marketing
                agency, you are an expert at taking amazing photographs that
                inspire and engage, you're now working on a new campaign for a super
                important customer and you need to take the most amazing photograph."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )

    def chief_creative_director_agent(self):
        return Agent(
            role="Chief Creative Director",
            goal=dedent("""\
                Oversee the work done by your team to make sure it's the best
                possible and aligned with the product's goals, review, approve,
                ask clarifying question or delegate follow up work if necessary to make
                decisions"""),
            backstory=dedent("""\
                You're the Chief Content Officer of leading digital
                marketing specialized in product branding. You're working on a new
                customer, trying to make sure your team is crafting the best possible
                content for the customer."""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_instagram
            ],
            llm=self.llm,
            verbose=True
        )


def create_ideation_team(additional_tools=None) -> dict:
    agent_factory = InstaContentFactory(additional_tools)
    return {
        "Product_Competitor_Analyst": agent_factory.product_competitor_agent(),
        "Strategy_Planner": agent_factory.strategy_planner_agent(),
        "Creative_Content_Creator": agent_factory.creative_content_creator_agent(),
        "Senior_Photographer": agent_factory.senior_photographer_agent(),
        "Chief_Creative_Director": agent_factory.chief_creative_director_agent()
    }