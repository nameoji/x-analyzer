import streamlit as st
import tweepy

# APIキー入力欄（StreamlitのUI）
st.title("🔍 X（Twitter）アカウント簡易診断ツール")
st.caption("※ あなた自身のAPIキーを入力してください。")

api_key = st.text_input("API Key", type="password")
api_secret = st.text_input("API Secret", type="password")
access_token = st.text_input("Access Token", type="password")
access_token_secret = st.text_input("Access Token Secret", type="password")

if st.button("診断開始！"):
    try:
        # 認証
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
        api = tweepy.API(auth)
        user = api.verify_credentials()

        # 表示
        st.success("✅ 認証成功！診断結果はこちら👇")
        st.write(f"🆔 ユーザー名：@{user.screen_name}")
        st.write(f"📛 表示名：{user.name}")
        st.write(f"👥 フォロー数：{user.friends_count}")
        st.write(f"👣 フォロワー数：{user.followers_count}")
        st.write(f"📝 ツイート数：{user.statuses_count}")
        st.write(f"🕰 最終ツイート日時：{user.status.created_at if user.status else 'ツイートなし'}")
        st.write(f"🔒 鍵アカウントか？：{'はい' if user.protected else 'いいえ'}")

    except Exception as e:
        st.error(f"❌ エラーが発生しました：{e}")
