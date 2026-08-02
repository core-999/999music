#99
import asyncio
import os
import base64
from typing import Optional

import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageFont, ImageFilter

from config import YOUTUBE_IMG_URL
from 999music.core.dir import CACHE_DIR


_FONT_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "default.ttf")


_thumb_session: Optional[aiohttp.ClientSession] = None
_thumb_session_lock = asyncio.Lock()

async def _get_session() -> aiohttp.ClientSession:
    global _thumb_session
    if _thumb_session and not _thumb_session.closed:
        return _thumb_session
    async with _thumb_session_lock:
        if _thumb_session and not _thumb_session.closed:
            return _thumb_session
        connector = aiohttp.TCPConnector(limit=32, ttl_dns_cache=300)
        timeout = aiohttp.ClientTimeout(total=15, sock_connect=5, sock_read=10)
        _thumb_session = aiohttp.ClientSession(connector=connector, timeout=timeout)
        return _thumb_session


def _draw_gradient_text(draw, x, y, text, font, color1, color2):
    """စာသား အရောင်စုံ"""
    dummy_img = Image.new("RGBA", (1, 1))
    dummy_draw = ImageDraw.Draw(dummy_img)
    
    current_x = x
    for char in text:
        char_bbox = dummy_draw.textbbox((0, 0), char, font=font)
        char_w = char_bbox[2] - char_bbox[0]
        char_h = char_bbox[3] - char_bbox[1]
        
        char_img = Image.new("RGBA", (char_w + 4, char_h + 4), (0, 0, 0, 0))
        char_draw = ImageDraw.Draw(char_img)
        char_draw.text((-char_bbox[0], -char_bbox[1]), char, fill=color1, font=font)
        
        draw.bitmap((current_x, y), char_img, fill=color2)
        current_x += char_w


async def get_thumb(videoid: str) -> str:
    cache_path = os.path.join(CACHE_DIR, f"{videoid}_card_v12.png")
    if os.path.exists(cache_path):
        return cache_path

    thumbnail_urls = [
        f"https://img.youtube.com/vi/{videoid}/maxresdefault.jpg",
        f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg",
        f"https://img.youtube.com/vi/{videoid}/sddefault.jpg",
        f"https://img.youtube.com/vi/{videoid}/mqdefault.jpg",
    ]

    session = await _get_session()
    thumb_path = os.path.join(CACHE_DIR, f"thumb{videoid}.jpg")
    downloaded = False

    for url in thumbnail_urls:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    async with aiofiles.open(thumb_path, "wb") as f:
                        await f.write(await resp.read())
                    downloaded = True
                    break
        except Exception:
            continue

    if not downloaded:
        return YOUTUBE_IMG_URL

    try:
        original_img = Image.open(thumb_path).convert("RGBA")
        
        
        bg_size = (1280, 720)
        bg = original_img.resize(bg_size, Image.Resampling.LANCZOS)
        bg = bg.filter(ImageFilter.GaussianBlur(35))
        
        
        darken = Image.new("RGBA", bg_size, (10, 10, 15, 90))
        bg = Image.alpha_composite(bg, darken)

        
        card_w, card_h = 800, 450
        card_img = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
        
        card_draw = ImageDraw.Draw(card_img)
        card_draw.rounded_rectangle(
            [0, 0, card_w, card_h],
            radius=20,
            fill=(25, 25, 35, 240),
            outline=(255, 255, 255, 80),
            width=3
        )

        inner_w, inner_h = 760, 410
        orig_w, orig_h = original_img.size
        if orig_w / orig_h > inner_w / inner_h:
            w_crop = int(orig_h * (inner_w / inner_h))
            img_cropped = original_img.crop(((orig_w - w_crop) // 2, 0, (orig_w + w_crop) // 2, orig_h))
        else:
            h_crop = int(orig_w * (inner_h / inner_w))
            img_cropped = original_img.crop((0, (orig_h - h_crop) // 2, orig_w, (orig_h + h_crop) // 2))
            
        yt_img = img_cropped.resize((inner_w, inner_h), Image.Resampling.LANCZOS)
        card_img.paste(yt_img, (20, 20))

        bg_w, bg_h = bg_size
        card_x = (bg_w - card_w) // 2
        card_y = (bg_h - card_h) // 2 - 15
        bg.paste(card_img, (card_x, card_y), card_img)

        
        bottom_code = "U09VUkNFIC0gQEhBTlRIQVI5OTkgQENPUkVTXzk5OQ==" 
        bottom_text = base64.b64decode(bottom_code).decode("utf-8")

        
        try:
            font_size_bottom = 28
            
            try:
                font_bottom = ImageFont.truetype(_FONT_PATH, font_size_bottom)
            except Exception:
                font_bottom = ImageFont.load_default()

            dummy_img = Image.new("RGBA", (1, 1))
            dummy_draw = ImageDraw.Draw(dummy_img)

            bbox_bottom = dummy_draw.textbbox((0, 0), bottom_text, font=font_bottom)
            w_bot = bbox_bottom[2] - bbox_bottom[0]
            h_bot = bbox_bottom[3] - bbox_bottom[1]

            x_bot = (bg_w - w_bot) // 2
            y_bot = bg_h - 65  

            draw = ImageDraw.Draw(bg)
            
            
            _draw_gradient_text(draw, x_bot, y_bot, bottom_text, font_bottom, (0, 255, 255, 255), (255, 100, 255, 255))

        except Exception as e:
            print(f"Error drawing text: {e}")
            pass

        final_img = bg.convert("RGB")
        final_img.save(cache_path, quality=95)
    except Exception:
        return YOUTUBE_IMG_URL
    finally:
        try:
            os.remove(thumb_path)
        except OSError:
            pass

    return cache_path



async def get_thumb_url(videoid: str) -> str:
    """Get thumbnail URL directly (NO download) - for Bot API colored buttons."""
    thumbnail_urls = [
        f"https://img.youtube.com/vi/{videoid}/maxresdefault.jpg",
        f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg",
        f"https://img.youtube.com/vi/{videoid}/sddefault.jpg",
    ]
    return thumbnail_urls[0]
