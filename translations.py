from config import ASSISTANT_NAME
from helpers.bot_utils import BOT_NAME, USERNAME


START_TEXT = f"👋🏻 **Hello**, \n\nĐây là **{BOT_NAME}** \nTôi có thể truyền phát trực tiếp, radio, video YouTube và tệp âm thanh / video Telegram trên trò chuyện thoại của các nhóm Telegram. Hãy cùng thưởng thức chế độ xem điện ảnh của trình phát video nhóm với bạn bè của bạn 😉!** 👑"
HELP_TEXT = f"""
🛠-- **Setting Up Bot**:--

\u2022 Bắt đầu trò chuyện thoại trong nhóm của bạn!
\u2022 Thêm tôi (@{USERNAME}) & trợ lý của tôi (@{ASSISTANT_NAME}) vào tới nhóm của bạn!
\u2022 Trao quyền quản trị cho tôi (@{USERNAME}) & trợ lý của tôi (@{ASSISTANT_NAME}) trong nhóm của bạn!

⚔️-- **Các lệnh có sẵn**:--

\u2022 `/play` - Stream An Audio
\u2022 `/stream` - Stream An Video
\u2022 `/pause` - Pause Current Stream
\u2022 `/resume` - Resume Paused Stream
\u2022 `/endstream` - End Stream & Left VC
\u2022 `/restart` - Restart Bot (Sudo Only)
"""
ABOUT_TEXT = f"💡-- **Information**:-- \n\nBot này được tạo để truyền phát video trong cuộc trò chuyện video nhóm telegram bằng một số phương pháp từ WebRTC. Được hỗ trợ bởi pytgcalls, API máy khách không đồng bộ cho Cuộc gọi nhóm Telegram và Pyrogram, Khung và Thư viện máy khách API MTProto của telegram trong Python thuần túy dành cho Người dùng và Bot. \n\n**Bot này được cấp phép theo Giấy phép GNU-GPL 3.0!**"
