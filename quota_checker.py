import os
import time
from langchain_google_genai import ChatGoogleGenerativeAI

def check_api_quota():
    """Simple function to test if API is accessible and not over quota"""
    try:
        print("Checking Google Gemini API quota...")
        
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key=os.environ.get('GOOGLE_API_KEY'),
            temperature=0.1,
            max_retries=1,
            request_timeout=10
        )
        
        # Simple test query
        response = llm.invoke("Say 'API is working' in exactly 3 words.")
        print(f"✅ API Response: {response}")
        print("✅ Quota check passed - API is accessible")
        return True
        
    except Exception as e:
        if "429" in str(e) or "ResourceExhausted" in str(e):
            print("❌ Quota exceeded - you need to wait or upgrade your plan")
            print("Check: https://ai.google.dev/gemini-api/docs/rate-limits")
        else:
            print(f"❌ API Error: {str(e)}")
        return False

def wait_for_quota_reset():
    """Wait for quota to reset with countdown"""
    print("Waiting for quota to reset...")
    for i in range(300, 0, -30):  # Wait 5 minutes with 30-second updates
        print(f"Waiting {i} seconds...")
        time.sleep(30)
    print("Attempting to check quota again...")

if __name__ == "__main__":
    print("=== Google Gemini API Quota Checker ===")
    
    # Check current status
    if not check_api_quota():
        print("\nOptions:")
        print("1. Wait for quota to reset (usually 1 minute)")
        print("2. Upgrade your Google Gemini API plan")
        print("3. Switch to a different API key if available")
        
        choice = input("\nWait for quota reset? (y/n): ").lower()
        if choice == 'y':
            wait_for_quota_reset()
            check_api_quota()
    else:
        print("\n✅ Ready to run the marketing crew!")