from flask_jwt_extended import decode_token

def get_email_from_cookie(cookie):
    try:
        # 토큰 디코딩
        decoded_token = decode_token(cookie)
        
        # 페이로드에서 email 값 추출
        email = decoded_token['sub']  # 'sub' 키 사용
        return email
    except Exception as e:
        print(f"Error decoding token: {e}")
        return None