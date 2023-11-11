import streamlit as st

def main():
    st.title("간단한 계산기")

    # 사용자로부터 숫자 입력 받기
    num1 = st.number_input("첫 번째 숫자를 입력하세요", value=0.0)
    num2 = st.number_input("두 번째 숫자를 입력하세요", value=0.0)

    # 연산 선택하기
    operation = st.selectbox("연산을 선택하세요", ["덧셈", "뺄셈", "곱셈", "나눗셈"])

    # 계산 수행
    result = calculate(num1, num2, operation)

    # 결과 출력
    st.write(f"결과: {result}")

def calculate(num1, num2, operation):
    if operation == "덧셈":
        return num1 + num2
    elif operation == "뺄셈":
        return num1 - num2
    elif operation == "곱셈":
        return num1 * num2
    elif operation == "나눗셈":
        if num2 != 0:
            return num1 / num2
        else:
            return "두 번째 숫자는 0이 될 수 없습니다."

if __name__ == "__main__":
    main()
