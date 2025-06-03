"""Professional visual asset management system for AI Engineer Portfolio"""
import random
import asyncio
from typing import List, Dict, Optional, Tuple
import requests
from pathlib import Path
import os

class ProfessionalAssetManager:
    """Manages professional visual assets for AI Engineer portfolio"""
    
    # AI and technology focused image categories
    AI_CATEGORIES = [
        "artificial intelligence", 
        "machine learning", 
        "data science", 
        "neural network", 
        "technology", 
        "code", 
        "algorithm", 
        "robotics",
        "deep learning",
        "computer vision"
    ]
    
    # Fallback image URLs if external services fail
    FALLBACK_IMAGES = [
        "https://picsum.photos/800/600?random=1",
        "https://picsum.photos/800/600?random=2",
        "https://picsum.photos/800/600?random=3",
        "https://picsum.photos/800/600?random=4",
        "https://picsum.photos/800/600?random=5"
    ]
    
    @staticmethod
    async def get_ai_image(index: int = 0, width: int = 800, height: int = 600) -> str:
        """
        Fetch contextually relevant professional AI-themed images
        
        Args:
            index: Index to select different categories
            width: Desired image width
            height: Desired image height
            
        Returns:
            URL to a professional AI-themed image
        """
        try:
            # Select category based on index
            category = ProfessionalAssetManager.AI_CATEGORIES[index % len(ProfessionalAssetManager.AI_CATEGORIES)]
            
            # Generate unique seed to avoid caching issues
            seed = random.randint(1000, 9999)
            
            # Format category for URL (replace spaces with plus signs)
            formatted_category = category.replace(" ", "+")
            
            # Construct Unsplash URL
            img_url = f"https://source.unsplash.com/{width}x{height}/?{formatted_category}&sig={seed}"
            
            # Add a small delay to prevent rate limiting and ensure different images
            await asyncio.sleep(0.1)
            
            return img_url
        except Exception as e:
            print(f"Error fetching AI image: {e}")
            # Fallback to a reliable placeholder
            fallback_index = index % len(ProfessionalAssetManager.FALLBACK_IMAGES)
            return ProfessionalAssetManager.FALLBACK_IMAGES[fallback_index]
    
    @staticmethod
    async def get_hero_image(width: int = 1200, height: int = 600) -> str:
        """
        Get high-quality hero image for main portfolio header
        
        Args:
            width: Desired image width
            height: Desired image height
            
        Returns:
            URL to a professional hero image
        """
        try:
            # Generate unique seed to avoid caching
            seed = random.randint(10000, 99999)
            
            # Use multiple AI-related terms for a more specific image
            return f"https://source.unsplash.com/{width}x{height}/?artificial+intelligence+technology+code&sig={seed}"
        except Exception as e:
            print(f"Error fetching hero image: {e}")
            return f"https://picsum.photos/{width}/{height}?random={random.randint(1, 1000)}"
    
    @staticmethod
    async def get_profile_image(width: int = 400, height: int = 400) -> str:
        """
        Get a professional profile image
        
        Args:
            width: Desired image width
            height: Desired image height
            
        Returns:
            URL to a professional profile image
        """
        try:
            seed = random.randint(5000, 9999)
            return f"https://source.unsplash.com/{width}x{height}/?professional+portrait+technology&sig={seed}"
        except Exception as e:
            print(f"Error fetching profile image: {e}")
            return f"https://picsum.photos/{width}/{height}?random={random.randint(1, 1000)}"
    
    @staticmethod
    def get_placeholder_svg(width: int, height: int, text: str = "AI Image") -> str:
        """
        Generates a simple SVG placeholder with AI-themed styling
        
        Args:
            width: SVG width
            height: SVG height
            text: Text to display in the placeholder
            
        Returns:
            SVG markup as a string
        """
        # AI-themed color scheme
        bg_color = "#1a2980"
        text_color = "#ffffff"
        
        return f"""<svg width='{width}' height='{height}' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {width} {height}'>
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a2980;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#26d0ce;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect fill='url(#grad)' width='{width}' height='{height}'/>
  <text x='50%' y='50%' dominant-baseline='middle' text-anchor='middle' font-family='sans-serif' font-size='24' fill='{text_color}'>{text}</text>
  <g fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="1">
    <path d="M0,{height/3} L{width},{height/3}" />
    <path d="M0,{height*2/3} L{width},{height*2/3}" />
    <path d="M{width/3},0 L{width/3},{height}" />
    <path d="M{width*2/3},0 L{width*2/3},{height}" />
  </g>
</svg>"""
    
    @staticmethod
    async def cache_images(categories: List[str], count: int = 1) -> Dict[str, List[str]]:
        """
        Pre-cache multiple images for different categories
        
        Args:
            categories: List of image categories to cache
            count: Number of images to cache per category
            
        Returns:
            Dictionary mapping categories to lists of image URLs
        """
        cached_images = {}
        
        for category in categories:
            category_images = []
            for i in range(count):
                try:
                    seed = random.randint(1000, 9999)
                    formatted_category = category.replace(" ", "+")
                    img_url = f"https://source.unsplash.com/800x600/?{formatted_category}&sig={seed}"
                    category_images.append(img_url)
                    await asyncio.sleep(0.1)  # Prevent rate limiting
                except Exception as e:
                    print(f"Error caching image for {category}: {e}")
                    fallback_index = i % len(ProfessionalAssetManager.FALLBACK_IMAGES)
                    category_images.append(ProfessionalAssetManager.FALLBACK_IMAGES[fallback_index])
            
            cached_images[category] = category_images
        
        return cached_images