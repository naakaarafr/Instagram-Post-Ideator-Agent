from dotenv import load_dotenv
load_dotenv()

from textwrap import dedent
from crewai import Agent, Crew, Process

from tasks import MarketingAnalysisTasks
from agents import InstaContentFactory

def main():
    tasks = MarketingAnalysisTasks()
    agents = InstaContentFactory()

    print("## Welcome to the Marketing Crew")
    print('-------------------------------')
    product_website = input("What is the product website you want a marketing strategy for?\n")
    product_details = input("Any extra details about the product and/or the Instagram post you want?\n")

    try:
        # Create Agents
        product_competitor_agent = agents.product_competitor_agent()
        strategy_planner_agent = agents.strategy_planner_agent()
        creative_agent = agents.creative_content_creator_agent()
        
        # Create Tasks
        website_analysis = tasks.product_analysis(product_competitor_agent, product_website, product_details)
        market_analysis = tasks.competitor_analysis(product_competitor_agent, product_website, product_details)
        campaign_development = tasks.campaign_development(strategy_planner_agent, product_website, product_details)
        write_copy = tasks.instagram_ad_copy(creative_agent)

        # Create Crew responsible for Copy
        copy_crew = Crew(
            agents=[
                product_competitor_agent,
                strategy_planner_agent,
                creative_agent
            ],
            tasks=[
                website_analysis,
                market_analysis,
                campaign_development,
                write_copy
            ],
            process=Process.sequential,
            verbose=True,
            memory=False,  # Disable memory to avoid conflicts
            max_rpm=10,    # Rate limiting
        )

        print("🚀 Starting copy generation...")
        ad_copy = copy_crew.kickoff()

        # Create Crew responsible for Image
        senior_photographer = agents.senior_photographer_agent()
        chief_creative_director = agents.chief_creative_director_agent()
        
        # Create Tasks for Image
        take_photo = tasks.take_photograph_task(senior_photographer, ad_copy, product_website, product_details)
        approve_photo = tasks.review_photo(chief_creative_director, product_website, product_details)

        image_crew = Crew(
            agents=[
                senior_photographer,
                chief_creative_director
            ],
            tasks=[
                take_photo,
                approve_photo
            ],
            process=Process.sequential,
            verbose=True,
            memory=False,  # Disable memory to avoid conflicts
            max_rpm=10,    # Rate limiting
        )

        print("📸 Starting image description generation...")
        image = image_crew.kickoff()

        # Print results
        print("\n\n########################")
        print("## Here is the result")
        print("########################\n")
        print("Your post copy:")
        print(ad_copy)
        print("\n\nYour image description:")
        print(image)
        
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        print("Please check your API keys and try again.")

if __name__ == "__main__":
    main()