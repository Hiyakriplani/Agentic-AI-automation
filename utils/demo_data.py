"""
Demo Data Module for CampaignPilot AI
Provides realistic sample AI outputs for Demo Mode so the application operates seamlessly without an OpenAI API key.
Includes pre-configured demo output for 'Campus Brew' and dynamic fallback generator for custom inputs.
"""

from typing import Dict, Any

def get_campus_brew_demo() -> Dict[str, Any]:
    """Return complete realistic pre-generated campaign output for 'Campus Brew'."""
    return {
        "requirements": {
            "product_name": "Campus Brew",
            "product_description": "Ready-to-drink premium bottled cold coffee for Gen-Z college students needing instant energy and focus.",
            "target_audience": "College students & young professionals",
            "age_group": "18–24",
            "location": "India",
            "budget": 20000,
            "currency": "₹",
            "duration_days": 15,
            "objective": "Brand Awareness",
            "platforms": ["Instagram", "Facebook"],
            "tone": "Fun and youthful"
        },
        "audience": {
            "primary_audience": "Gen-Z college students (18-22) attending universities in Indian metro and Tier-1 cities.",
            "secondary_audience": "Young freelancers and exam prep students (22-24) working late nights.",
            "audience_interests": [
                "Campus lifestyle & memes",
                "Late-night study sessions & exam hustle",
                "Trending Instagram Reels & pop culture",
                "Affordable cold coffee beverages"
            ],
            "pain_points": [
                "Sluggish energy during afternoon lectures and late-night study marathons",
                "High price of fancy cafe cold coffees",
                "Messy preparation of instant coffee in hostel rooms"
            ],
            "buying_motivation": "Instant convenience, trendy aesthetic bottle to carry on campus, and budget-friendly caffeine boost.",
            "recommended_communication_style": "Witty, relatable, meme-inspired, high-energy, using Gen-Z campus lingo and vibrant visuals."
        },
        "strategy": {
            "campaign_objective": "Build explosive brand awareness and viral campus buzz for Campus Brew within 15 days.",
            "core_strategy": "Leverage relatable exam/lecture struggle memes paired with high-tempo Instagram Reels and student ambassador giveaways to establish Campus Brew as the official fuel of college life.",
            "unique_campaign_idea": "#SipTheHustle - The Ultimate Campus Fuel",
            "key_message": "Don't let 8 AM lectures win. Chill out and fuel up with Campus Brew!",
            "recommended_platforms": ["Instagram (Primary - 70%)", "Facebook (Secondary - 30%)"],
            "platform_strategy": {
                "Instagram": "Focus on high-energy Reels, meme carousels, student poll stories, and UGC giveaways.",
                "Facebook": "Target college community groups, student hostel pages, and local event promotions."
            },
            "content_mix": "40% Memes & Humor, 30% Product Spotlights & Taste Test Reels, 20% UGC Contests, 10% Promotional Discounts."
        },
        "content": [
            {
                "id": 1,
                "platform": "Instagram",
                "content_type": "Reel Video",
                "topic": "8 AM Lecture Vs Cold Coffee Reality",
                "hook": "Me entering the 8 AM lecture after sleeping at 4 AM... 💀",
                "caption": "When the professor starts calling attendance and your brain is still in sleep mode. 😴 One chilled bottle of Campus Brew and you're back in the game! Grab yours at the campus canteen now. ☕⚡",
                "cta": "Tag your sleep-deprived study partner in the comments!",
                "hashtags": "#CampusBrew #SipTheHustle #CollegeLife #ColdCoffee #ExamHustle #GenZMemes"
            },
            {
                "id": 2,
                "platform": "Instagram",
                "content_type": "Meme Carousel",
                "topic": "Types of Students During Exam Week",
                "hook": "Which student are you during exam season? Swipe to find out! ➡️",
                "caption": "1. The All-Nighter Pro 🌙 2. The Panic Reader 📑 3. The Guy Powered by 3 Bottles of Campus Brew ☕🔥 No matter your study style, Campus Brew has your back!",
                "cta": "Comment your score out of 10 for exam readiness below!",
                "hashtags": "#CampusBrew #ExamSeason #CollegeMemes #IndiaColleges #ColdCoffeeBoost"
            },
            {
                "id": 3,
                "platform": "Facebook",
                "content_type": "Image Post & Giveaway Announcement",
                "topic": "#SipTheHustle Campus Crew Giveaway",
                "hook": "WIN 1 MONTH OF FREE COLD COFFEE FOR YOUR HOSTEL BLOCK! 🎉",
                "caption": "We are giving away 50 bottles of Campus Brew to the coolest hostel group! All you have to do is like this post, tag 3 friends, and tell us your funniest hostel memory!",
                "cta": "Click the link to enter the #SipTheHustle Hostel Contest!",
                "hashtags": "#CampusBrewGiveaway #HostelLife #FreeCoffee #CollegeContest #CampusBrew"
            },
            {
                "id": 4,
                "platform": "Instagram",
                "content_type": "Story Poll & Quiz",
                "topic": "Flavour Battle: Dark Roast vs Hazelnut",
                "hook": "Which Campus Brew flavour gives you maximum exam focus? 🔥",
                "caption": "Team Classic Dark Roast 🖤 or Team Creamy Hazelnut 🌰? Vote on our story poll and get an instant 15% discount coupon for your next order!",
                "cta": "Tap the sticker to vote now!",
                "hashtags": "#CampusBrew #Poll #CoffeeBattle #CampusVibes"
            },
            {
                "id": 5,
                "platform": "Facebook",
                "content_type": "Video Post (Student Testimonial)",
                "topic": "Hostel Room Coffee Recipe vs Campus Brew",
                "hook": "Making instant coffee in a hostel kettle vs opening a chilled Campus Brew 😭",
                "caption": "Stop burning your hands with messy hostel kettles and lukewarm milk. Campus Brew comes ice-cold, perfectly brewed, and ready to drink instantly!",
                "cta": "Order a 6-pack bundle on our website today!",
                "hashtags": "#HostelHacks #CampusBrew #ColdCoffeeIndia #ReadyToDrink #StudentLife"
            }
        ],
        "budget": {
            "total_budget": 20000,
            "currency": "₹",
            "allocations": [
                {
                    "category": "Social Media Advertising",
                    "amount": 9000,
                    "percentage": 45.0,
                    "description": "Targeted Instagram & Facebook micro-ads focusing on students within 5km radius of top college campuses."
                },
                {
                    "category": "Content Creation",
                    "amount": 4000,
                    "percentage": 20.0,
                    "description": "High-quality video editing, graphic design for meme carousels, and product photography."
                },
                {
                    "category": "Influencer Marketing",
                    "amount": 5000,
                    "percentage": 25.0,
                    "description": "Collaborations with 5 campus micro-influencers and college meme page creators."
                },
                {
                    "category": "Promotional Activities",
                    "amount": 2000,
                    "percentage": 10.0,
                    "description": "Free product tasting samples distributed during college fest entrance."
                }
            ]
        },
        "schedule": [
            {"day": 1, "date": "Day 1", "platform": "Instagram", "content_type": "Reel Video", "topic": "8 AM Lecture Vs Cold Coffee Reality", "objective": "Brand Awareness & Reach"},
            {"day": 2, "date": "Day 2", "platform": "Facebook", "content_type": "Image Post", "topic": "#SipTheHustle Giveaway Teaser", "objective": "Audience Engagement"},
            {"day": 3, "date": "Day 3", "platform": "Instagram", "content_type": "Story Poll", "topic": "Flavour Battle: Dark Roast vs Hazelnut", "objective": "Interactive Engagement"},
            {"day": 4, "date": "Day 4", "platform": "Instagram", "content_type": "Meme Carousel", "topic": "Types of Students During Exam Week", "objective": "Virality & Shares"},
            {"day": 5, "date": "Day 5", "platform": "Facebook", "content_type": "Video Post", "topic": "Hostel Room Coffee Recipe vs Campus Brew", "objective": "Consideration"},
            {"day": 6, "date": "Day 6", "platform": "Instagram", "content_type": "Reel Video", "topic": "Campus Micro-Influencer Taste Test", "objective": "Social Proof"},
            {"day": 7, "date": "Day 7", "platform": "Facebook", "content_type": "Giveaway Post", "topic": "Hostel Block Giveaway Winner Announcement", "objective": "Community Building"},
            {"day": 8, "date": "Day 8", "platform": "Instagram", "content_type": "Meme Post", "topic": "When Professor Says 'Attendance is Compulsory'", "objective": "Brand Recall"},
            {"day": 9, "date": "Day 9", "platform": "Instagram", "content_type": "Story Quiz", "topic": "Guess the Caffeine Level!", "objective": "Interaction"},
            {"day": 10, "date": "Day 10", "platform": "Facebook", "content_type": "Carousel", "topic": "Top 5 Places to Study on Campus with Campus Brew", "objective": "Local Engagement"},
            {"day": 11, "date": "Day 11", "platform": "Instagram", "content_type": "Reel Video", "topic": "Behind The Scenes: Chilling the Brew", "objective": "Authenticity"},
            {"day": 12, "date": "Day 12", "platform": "Instagram", "content_type": "Promo Post", "topic": "Exams Special: Buy 2 Get 1 Free Bundle", "objective": "Direct Sales Lead"},
            {"day": 13, "date": "Day 13", "platform": "Facebook", "content_type": "Video Post", "topic": "Student Testimonial: Surviving Semester Exams", "objective": "Trust Building"},
            {"day": 14, "date": "Day 14", "platform": "Instagram", "content_type": "Story Countdowns", "topic": "Last 24 Hours of Campus Offer", "objective": "Urgency & Conversion"},
            {"day": 15, "date": "Day 15", "platform": "Instagram & FB", "content_type": "Thank You Reel", "topic": "Campus Brew Crew Highlights & Recap", "objective": "Brand Loyalty"}
        ],
        "kpis": {
            "recommendations": [
                {
                    "kpi_name": "Total Organic & Paid Reach",
                    "why_it_matters": "Measures how many unique college students saw the campaign across target campuses.",
                    "target_range": "35,000 - 50,000 Impressions",
                    "how_measured": "Instagram Insights & Facebook Ads Manager reach metrics."
                },
                {
                    "kpi_name": "Engagement Rate",
                    "why_it_matters": "Indicates how relatable and shareable the meme Reels and campus content are.",
                    "target_range": "6.5% - 8.5% Engagement",
                    "how_measured": "(Likes + Comments + Shares + Saves) / Total Reach * 100."
                },
                {
                    "kpi_name": "Click-Through Rate (CTR)",
                    "why_it_matters": "Evaluates how effectively social ads drive traffic to the product landing page or online canteen order link.",
                    "target_range": "2.2% - 3.4% CTR",
                    "how_measured": "Link Clicks / Ad Impressions."
                },
                {
                    "kpi_name": "Hostel Giveaway Leads",
                    "why_it_matters": "Collects direct student contacts and hostel block referrals for future promotions.",
                    "target_range": "250 - 400 Qualified Entries",
                    "how_measured": "Form submissions on giveaway landing page."
                },
                {
                    "kpi_name": "Instagram Follower Growth",
                    "why_it_matters": "Establishes a lasting audience base for future seasonal launches.",
                    "target_range": "+1,200 New Campus Followers",
                    "how_measured": "Net follower change in Instagram professional dashboard."
                }
            ]
        }
    }

def generate_generic_demo(requirements: Dict[str, Any]) -> Dict[str, Any]:
    """Generate dynamic demo output for any custom user input when in Demo Mode."""
    product = requirements.get("product_name", "Our Brand")
    desc = requirements.get("product_description", "High quality product")
    audience = requirements.get("target_audience", "General Consumers")
    obj = requirements.get("objective", "Brand Awareness")
    budget = float(requirements.get("budget", 10000))
    duration = int(requirements.get("duration_days", 14))
    platforms = requirements.get("platforms", ["Instagram", "LinkedIn"])
    tone = requirements.get("tone", "Professional")

    # If product is campus brew or similar, return the specialized demo
    if "campus brew" in product.lower():
        return get_campus_brew_demo()

    p_str = ", ".join(platforms) if platforms else "Social Media"
    p1 = platforms[0] if platforms else "Instagram"
    p2 = platforms[1] if len(platforms) > 1 else p1

    return {
        "requirements": requirements,
        "audience": {
            "primary_audience": f"Primary segment of {audience} interested in modern solutions and premium value.",
            "secondary_audience": f"Secondary audience of enthusiastic early adopters aged {requirements.get('age_group', '18-35')}.",
            "audience_interests": ["Industry innovation", "Quality products", "Social recommendations", "Convenient digital ordering"],
            "pain_points": [
                f"Lack of efficient options matching the needs of {audience}",
                "High pricing or inconsistent product quality from competitors",
                "Complicated purchasing process"
            ],
            "buying_motivation": f"Seeking reliability, superior quality, and value delivered with a {tone.lower()} brand approach.",
            "recommended_communication_style": f"{tone} messaging tailored with impactful visuals and clear value propositions."
        },
        "strategy": {
            "campaign_objective": f"Drive significant {obj} for {product} over a {duration}-day period.",
            "core_strategy": f"Deploy multi-channel campaign across {p_str}, highlighting key benefits of {desc[:60]}...",
            "unique_campaign_idea": f"#{product.replace(' ', '')}Excellence Campaign",
            "key_message": f"Transform your daily experience with {product}.",
            "recommended_platforms": platforms,
            "platform_strategy": {p: f"Tailor content specifically for {p} users with consistent visual branding." for p in platforms},
            "content_mix": "35% Educational/Product Demos, 35% Customer Stories & Reviews, 20% Promotional Offers, 10% Interactive Q&As."
        },
        "content": [
            {
                "id": 1,
                "platform": p1,
                "content_type": "Feature Spotlight Video",
                "topic": f"Introducing {product}",
                "hook": f"Discover the smarter way to experience {product}!",
                "caption": f"Say goodbye to old routines. {product} brings you top-tier quality designed specifically for {audience}. Check out what makes us different today! 🚀",
                "cta": "Click the link in bio to learn more!",
                "hashtags": f"#{product.replace(' ', '')} #{obj.replace(' ', '')} #Innovation #Quality"
            },
            {
                "id": 2,
                "platform": p2,
                "content_type": "Infographic Carousel",
                "topic": f"Top 3 Reasons {audience} Choose {product}",
                "hook": "Swipe to see how we solve your biggest daily challenges ➡️",
                "caption": f"We built {product} after listening to what {audience} truly needed. Swipe through to discover our core features!",
                "cta": "Save this post for later!",
                "hashtags": f"#{product.replace(' ', '')} #SmartChoice #Solutions"
            },
            {
                "id": 3,
                "platform": p1,
                "content_type": "Customer Case Study / Review",
                "topic": "Real Results from Real Users",
                "hook": "Here's what happened when our first 100 customers made the switch...",
                "caption": f"Quality speaks for itself! See why {audience} love using {product} every day.",
                "cta": "Share your story in the comments below!",
                "hashtags": f"#{product.replace(' ', '')} #CustomerReview #ProvenResults"
            },
            {
                "id": 4,
                "platform": p2,
                "content_type": "Interactive Poll / Q&A",
                "topic": f"What's your biggest priority when picking a product?",
                "hook": "We want to hear from YOU! Cast your vote below 👇",
                "caption": "Vote in our story poll and get an exclusive discount code delivered straight to your DMs!",
                "cta": "Tap to cast your vote!",
                "hashtags": f"#{product.replace(' ', '')} #Poll #Community"
            },
            {
                "id": 5,
                "platform": p1,
                "content_type": "Promotional Launch Offer",
                "topic": f"Limited-Time Launch Special for {product}",
                "hook": "Don't miss out on our special launch discount! ⏳",
                "caption": f"To celebrate our {duration}-day campaign, get 15% off your first order of {product}!",
                "cta": "Use code LAUNCH15 at checkout today!",
                "hashtags": f"#{product.replace(' ', '')} #SpecialOffer #Discount"
            }
        ],
        "budget": {
            "total_budget": budget,
            "currency": "₹" if "india" in requirements.get("location", "").lower() else "$",
            "allocations": [
                {"category": "Social Media Advertising", "amount": round(budget * 0.45, 2), "percentage": 45.0, "description": f"Paid ad campaigns on {p_str} targeting {audience}."},
                {"category": "Content Creation", "amount": round(budget * 0.25, 2), "percentage": 25.0, "description": "High resolution graphics, copywriting, and video production."},
                {"category": "Influencer Marketing", "amount": round(budget * 0.20, 2), "percentage": 20.0, "description": "Key opinion leaders and niche creator partnerships."},
                {"category": "Promotional Activities", "amount": round(budget * 0.10, 2), "percentage": 10.0, "description": "Special launch incentives, giveaways, and discount codes."}
            ]
        },
        "schedule": [
            {"day": i, "date": f"Day {i}", "platform": platforms[(i - 1) % len(platforms)], "content_type": "Post / Reel", "topic": f"Campaign Focus Part {i}", "objective": obj}
            for i in range(1, duration + 1)
        ],
        "kpis": {
            "recommendations": [
                {
                    "kpi_name": "Target Reach",
                    "why_it_matters": "Determines total brand exposure among target demographics.",
                    "target_range": f"{int(budget * 1.5):,} - {int(budget * 2.5):,} Impressions",
                    "how_measured": "Ad manager and platform analytics metrics."
                },
                {
                    "kpi_name": "Engagement Rate",
                    "why_it_matters": "Measures how actively your audience interacts with campaign posts.",
                    "target_range": "4.5% - 7.0%",
                    "how_measured": "Total interactions divided by reach."
                },
                {
                    "kpi_name": "Click-Through Rate (CTR)",
                    "why_it_matters": "Evaluates how effectively ad copy converts views into link clicks.",
                    "target_range": "1.8% - 3.2%",
                    "how_measured": "Clicks divided by impressions."
                },
                {
                    "kpi_name": "Estimated Conversion / Leads",
                    "why_it_matters": "Tracks direct business impact and customer acquisitions.",
                    "target_range": f"{int(budget * 0.02):,} - {int(budget * 0.05):,} Leads",
                    "how_measured": "Website conversions / Sign-up form completions."
                }
            ]
        }
    }
