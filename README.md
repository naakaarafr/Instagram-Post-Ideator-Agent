# Instagram Post Ideator Agent 🚀

An intelligent multi-agent system powered by Google Gemini that creates compelling Instagram marketing content through automated product analysis, competitor research, and creative content generation.

## 🎯 What This Project Does

This AI-powered marketing crew analyzes your product, researches competitors, develops marketing strategies, and generates both **Instagram ad copy** and **detailed photo descriptions** for your campaigns. It's like having a full marketing team working 24/7!

### Key Features

- **Automated Product Analysis**: Deep-dive analysis of your product's unique features and market positioning
- **Competitor Intelligence**: Identifies and analyzes top 3 competitors with strategic insights
- **Marketing Strategy Development**: Creates targeted campaign strategies tailored to your audience
- **Instagram Ad Copy Generation**: Produces 3 compelling copy options for your posts
- **Professional Photo Descriptions**: Generates 3 detailed photograph concepts for visual content
- **Multi-Agent Collaboration**: 5 specialized AI agents working together seamlessly

## 🤖 Meet Your AI Marketing Team

### 1. **Lead Market Analyst** 📊
- Conducts comprehensive product and competitor analysis
- Provides strategic market insights
- Identifies unique selling propositions

### 2. **Chief Marketing Strategist** 🎯
- Synthesizes research into actionable marketing strategies
- Develops campaign concepts and audience targeting
- Creates strategic frameworks for content creation

### 3. **Creative Content Creator** ✍️
- Crafts engaging Instagram ad copy
- Develops compelling narratives that resonate with audiences
- Transforms strategies into actionable creative content

### 4. **Senior Photographer** 📸
- Creates detailed descriptions for Instagram-worthy photographs
- Focuses on emotion-driven visual concepts
- Designs images that capture attention and convey brand messages

### 5. **Chief Creative Director** 🎨
- Reviews and approves all creative work
- Ensures alignment with brand goals and campaign objectives
- Provides final quality control and strategic oversight

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+
- Google Gemini API Key
- Serper API Key (for web scraping and search)

### Step 1: Clone the Repository

```bash
git clone https://github.com/naakaarafr/instagram-post-ideator-agent.git
cd instagram-post-ideator-agent
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Environment Setup

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

### Step 4: Get Your API Keys

#### Google Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy and add to your `.env` file

#### Serper API Key (for web search)
1. Visit [Serper.dev](https://serper.dev)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Add to your `.env` file

## 🚀 Usage

### Quick Start

```bash
python crew.py
```

### Interactive Process

1. **Enter Product Website**: Provide the URL of the product you want to market
2. **Add Extra Details**: Include any specific requirements or product details
3. **Wait for Magic**: The AI agents will work together to analyze and create content
4. **Get Results**: Receive Instagram ad copy options and photo descriptions

### Example Run

```
## Welcome to the Marketing Crew
-------------------------------
What is the product website you want a marketing strategy for?
> https://example-product.com

Any extra details about the product and/or the Instagram post you want?
> Focus on eco-friendly aspects, target young professionals

🚀 Starting copy generation...
📸 Starting image description generation...

########################
## Here is the result
########################

Your post copy:
[Three compelling Instagram ad copy options]

Your image description:
[Three professional photo concept descriptions]
```

## 📁 Project Structure

```
instagram-post-ideator-agent/
│
├── agents.py           # AI agent definitions and factory
├── tasks.py           # Task definitions for each agent
├── crew.py            # Main execution script
├── config.py          # Configuration and API key management
├── tools.py           # Web scraping and search tools
├── quota_checker.py   # API quota monitoring utility
├── .env              # Environment variables (you create this)
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## 🔧 Configuration Options

### Model Settings (config.py)

- **Model**: Gemini 2.0 Flash (optimized for speed and efficiency)
- **Temperature**: 0.1 (for consistent, focused outputs)
- **Max Tokens**: 2048 (balanced for comprehensive responses)
- **Rate Limiting**: 10 RPM (requests per minute)

### Customization Options

- **Agent Tools**: Each agent can be equipped with additional custom tools
- **Task Descriptions**: Easily modify task prompts in `tasks.py`
- **Process Flow**: Sequential processing ensures quality and consistency

## 🛡️ API Quota Management

### Check Your Quota Status

```bash
python quota_checker.py
```

This utility helps you:
- Test API connectivity
- Monitor quota usage
- Get alerts before hitting limits
- Troubleshoot API issues

### Best Practices

- Monitor your API usage regularly
- Use the quota checker before large campaigns
- Consider upgrading your Gemini API plan for heavy usage
- The system includes built-in rate limiting (10 RPM)

## 📊 Output Examples

### Instagram Ad Copy Sample
```
🌱 Ready to transform your daily routine? 
Our eco-friendly essentials aren't just products—they're your gateway to conscious living. 
Join thousands of young professionals making a difference, one choice at a time. 
✨ Sustainable • Stylish • Smart
👆 Tap to start your green journey
#EcoLiving #SustainableLife #YoungProfessionals
```

### Photo Description Sample
```
A young professional in a modern minimalist office, 
holding a sleek eco-friendly product with natural sunlight 
streaming through large windows, creating soft shadows on 
a clean white desk with green plants in the background, 
shot with shallow depth of field, 4k crisp detail, 
professional lifestyle photography
```

## 🎨 Advanced Features

### Multi-Crew Architecture
The system runs two separate crews:
1. **Copy Crew**: Handles analysis, strategy, and copywriting
2. **Image Crew**: Focuses on visual concept development and approval

### Memory Management
- Memory disabled to prevent conflicts and ensure fresh analysis
- Each session starts with clean agent states
- Optimized for consistent, reliable outputs

### Error Handling
- Comprehensive error catching and user-friendly messages
- API failure recovery mechanisms
- Detailed logging for troubleshooting

## 🔍 Troubleshooting

### Common Issues

**API Key Errors**
- Ensure both API keys are correctly set in `.env`
- Check that your Gemini API key has sufficient quota
- Verify Serper API key is active

**Quota Exceeded**
- Run `python quota_checker.py` to check status
- Wait for quota reset (usually 1 minute for Gemini)
- Consider upgrading your API plan

**Slow Performance**
- Check your internet connection
- Verify API endpoints are accessible
- Rate limiting may cause delays (this is normal)

**Empty Results**
- Ensure the product website is accessible
- Try providing more detailed product information
- Check that the website contains meaningful content

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the Repository**
2. **Create a Feature Branch**: `git checkout -b feature/amazing-feature`
3. **Commit Changes**: `git commit -m 'Add amazing feature'`
4. **Push to Branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test with different product types
- Update documentation for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CrewAI**: For the excellent multi-agent framework
- **Google Gemini**: For powerful AI capabilities
- **Serper**: For reliable web scraping and search services
- **LangChain**: For seamless AI model integration

## 📞 Support

Having issues? Here's how to get help:

1. **Check the Troubleshooting section** above
2. **Run the quota checker**: `python quota_checker.py`
3. **Open an issue** on GitHub with detailed error information
4. **Contact**: [@naakaarafr](https://github.com/naakaarafr)

---

## 🚀 Ready to Get Started?

1. Set up your API keys
2. Install dependencies
3. Run `python crew.py`
4. Watch your AI ideation team create amazing content!

*Transform your Instagram marketing with the power of AI. Your products deserve the best content ideas - let our AI agent team deliver them.*
