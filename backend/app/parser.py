def mock_llm_parser(text: str):
    lower_text = text.lower()
    
    # Priority logic
    priority = "medium"
    if "urgent" in lower_text or "asap" in lower_text:
        priority = "high"
    elif "whenever" in lower_text or "low priority" in lower_text:
        priority = "low"
        
    # Date hint logic
    due_date_hint = None
    date_keywords = ["today", "tomorrow", "next week", "next monday", "next tuesday", "next wednesday", "next thursday", "next friday", "next saturday", "next sunday"]
    for kw in date_keywords:
        if kw in lower_text:
            due_date_hint = kw
            break
            
    # Title stripping
    title = text
    keywords_to_strip = ["urgent", "asap", "whenever", "low priority", "today", "tomorrow", "next week", 
                         "next monday", "next tuesday", "next wednesday", "next thursday", "next friday", "next saturday", "next sunday"]
    
    for kw in keywords_to_strip:
        title = title.replace(kw, "")
        
    title = title.strip()
    if not title:
        title = "Untitled task"
        
    return {
        "title": title,
        "priority": priority,
        "due_date_hint": due_date_hint
    }