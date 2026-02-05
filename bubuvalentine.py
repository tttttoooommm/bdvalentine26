import streamlit as st
import random
import time

st.set_page_config(page_title="A Special Question", page_icon="❤️")

st.header("Bianca, wöttsch min Valentine sie? ❤️")

# 1. The "Yes" Logic
if st.button("JA! 😍", use_container_width=True):
    st.balloons()
    gifs = [
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWpyMnRnMjRnNHNsb3FmOHN0bzM2cGJtMXQ4OGJwcWU1ODJ5NGtndyZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/MDJ9IbxxvDUQM/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3UyZ2xqbWJ3Y3dpa3B0MHEwZ3NldHRsYno5MXltZWZmcXl0YTJuciZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Lv2VhwHrt6ljhvZ6LF/giphy.gif"
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnFtcDdraHBpNjl2Mnh1OHdjN3R4aTMwOGo2emVmbW4xZmVlcTQ5aiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ytu2GUYbvhz7zShGwS/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZzY4Y3dpdzhpcDRkbmkwbmo5eHl3cWxxcmM4N2lma3Boa2dkNTV0biZlcD12MV9naWZzX3NlYXJjaCZjdD1n/R6gvnAxj2ISzJdbA63/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZzY4Y3dpdzhpcDRkbmkwbmo5eHl3cWxxcmM4N2lma3Boa2dkNTV0biZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PuTSgeacS3Z7i/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzNib2lmMnRqODRjM3UwY216a2h2NXo3dDd3Y3B5aGhyMHo3MXRlNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/WK7omsLop0431tZjXb/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHl3cDcxOG4zbzV0d3owZ3U4MXd1eW82Y29uYXlyZWd6NGRybGtoeSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/7k3ThwwMXnHCE/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnFtcDdraHBpNjl2Mnh1OHdjN3R4aTMwOGo2emVmbW4xZmVlcTQ5aiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/8QbwUh40Hl96yMgvOx/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2t6d2RnazNvM2MwYzk5bHoza2gwcTJkMmhzeDQ4cDRtZGZtcGN5eSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/TCKxvBY0MA3uKzXdeo/giphy.gif",
        "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmQycmNkc21xOWZ1aTdqemtsaHRrdzVhZ3BtMnBic25idW9xa2kzeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YxKXWOhTSq8I14NKEn/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dm8xOXU1amZuYnl2aWpyZTEwb3E3OWszNzFkd2FvY2ZqazYyMW1oNCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/3ofT5ySFXZ01oJ7aoM/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dm8xOXU1amZuYnl2aWpyZTEwb3E3OWszNzFkd2FvY2ZqazYyMW1oNCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/7W1rgKAxlDe3m/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnFtcDdraHBpNjl2Mnh1OHdjN3R4aTMwOGo2emVmbW4xZmVlcTQ5aiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/1JmGiBtqTuehfYxuy9/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dm8xOXU1amZuYnl2aWpyZTEwb3E3OWszNzFkd2FvY2ZqazYyMW1oNCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/kcZPBnwMkbKSgdTdK9/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3OHVuYmR2d2NjZDZ1d2FicXl6N3hyNWxmbHJ4a3kzajczN3puM3pidiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/IVK6xNBpEAHYyOdghk/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXNpb3FqaW4yZDE5cGUxZnptMDZxMHN6MHIxYWR4ZXlybGhlaGg0YSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Zl7u48zLVFgLpRwq6f/giphy.gif"
    ]

    # Initialize the HTML string
    container = st.empty()
    overlay_html = '<div style="position: relative; height: 600px; width: 100%;">'

    for i, url in enumerate(gifs):
        z_index = i + 1
        
        # Build the <img> tag string
        overlay_html += f'<img src="{url}" style="position: absolute; top: {random.randint(30, 150)}px; left: {random.randint(0,100)}%; transform: translateX(-50%); z-index: {z_index}; box-shadow: 10px 10px 20px rgba(0,0,0,0.2);">'
        container.markdown(overlay_html + '</div>', unsafe_allow_html=True)
        time.sleep(1.5)
    

    st.success("Yippie! Ich han gwüsst ds du ja sege wirsh! love you!")

# 2. The "No" Logic (Impossible Button)
no_button_js = """
<div id="container" style="height: 300px; width: 100%; position: relative;">
    <button id="noButton" style="position: absolute; left: 50%; top: 50%; padding: 10px 20px; background-color: #ff4b4b; color: white; border: none; border-radius: 5px; cursor: pointer;">
        Nei 😢
    </button>
</div>

<script>
    const btn = document.getElementById('noButton');
    const container = document.getElementById('container');

    btn.addEventListener('mouseover', function() {
        const newTop = Math.random() * (container.offsetHeight - btn.offsetHeight);
        const newLeft = Math.random() * (container.offsetWidth - btn.offsetWidth);
        btn.style.top = newTop + 'px';
        btn.style.left = newLeft + 'px';
    });

    btn.addEventListener('click', function() {
        alert("Hä wie hesh das überhaupt gschafft?");
        
        // Correct way to add an image via JavaScript:
        const img = document.createElement('img');
        img.src = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXN1OTd6MzNpeDI5MXJyMDdxa2cyN2lnbXpndzB1azFoYXV2eHFjNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/lkdH8FmImcGoylv3t3/giphy.gif";
        img.style.position = "absolute";
        img.style.top = "100px";
        img.style.left = "50%";
        img.style.transform = "translateX(-50%)";
        img.style.width = "200px";
        
        container.appendChild(img);


    });

</script>
"""
st.components.v1.html(no_button_js, height=400)