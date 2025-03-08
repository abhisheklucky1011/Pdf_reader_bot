css = '''
<style>
/* Chat Container */
.chat-message {
    padding: 1.5rem;
    border-radius: 0.75rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    transition: transform 0.2s ease-in-out, box-shadow 0.3s ease-in-out;
    backdrop-filter: blur(10px);
    background: rgba(255, 255, 255, 0.1);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

/* User Message */
.chat-message.user {
    background: linear-gradient(135deg, #1e3a8a, #3b82f6);
    border-left: 5px solid #4f46e5;
}

/* Bot Message */
.chat-message.bot {
    background: linear-gradient(135deg, #047857, #10b981);
    border-left: 5px solid #34d399;
}

/* Hover Effect */
.chat-message:hover {
    transform: scale(1.03);
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
}

/* Avatar Styling */
.chat-message .avatar {
    width: 65px;
    height: 65px;
    border-radius: 50%;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    background: rgba(255, 255, 255, 0.2);
    padding: 6px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    transition: transform 0.2s ease-in-out;
}

.chat-message .avatar:hover {
    transform: scale(1.1);
}

/* Avatar Image */
.chat-message .avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}

/* Message Content */
.chat-message .message {
    flex: 1;
    padding: 0 1rem;
    color: #f9fafb;
    font-size: 1rem;
    line-height: 1.6;
    font-weight: 500;
    word-wrap: break-word;
    max-width: 90%;
}

/* Responsive Design */
@media (max-width: 600px) {
    .chat-message {
        flex-direction: column;
        align-items: flex-start;
        padding: 1rem;
    }

    .chat-message .avatar {
        width: 50px;
        height: 50px;
    }

    .chat-message .message {
        width: 100%;
        padding: 0.5rem;
    }
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.postimg.cc/MZrKjS00/Bot-Image.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.postimg.cc/02Tkc0Bb/User-Image.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''