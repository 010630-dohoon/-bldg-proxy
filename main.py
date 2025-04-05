from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get-building-name', methods=['GET'])
def get_building_name():
    SERVICE_KEY = "MrVDw1GpFYZDIUkjsa8GHTTzfiy9H8CVSKLe8otH2cQmSnzbaQYnUC5TCrXBXQghAVe49Fcj60zCwXa35XB2xw=="

    # 주소 파라미터 받기
    sigunguCd = request.args.get('sigunguCd', '11680')
    bjdongCd = request.args.get('bjdongCd', '10300')
    platGbCd = request.args.get('platGbCd', '0')
    bun = request.args.get('bun', '0035')
    ji = request.args.get('ji', '0003')

    url = "https://apis.data.go.kr/1613000/BldRgstHubService/getBrTitleInfo"
    params = {
        "serviceKey": SERVICE_KEY,
        "sigunguCd": sigunguCd,
        "bjdongCd": bjdongCd,
        "platGbCd": platGbCd,
        "bun": bun,
        "ji": ji,
        "numOfRows": 10,
        "pageNo": 1,
        "_type": "json"
    }

    try:
        res = requests.get(url, params=params, timeout=5)
        data = res.json()
        items = data['response']['body']['items']['item']
        bldNm = items[0].get('bldNm', '이름 없음') if isinstance(items, list) else items.get('bldNm', '이름 없음')
        return jsonify({"bldNm": bldNm})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
