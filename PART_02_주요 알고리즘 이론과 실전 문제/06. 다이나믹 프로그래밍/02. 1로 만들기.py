x = int(input())

# 문제에서 정수 x는 최대 30000까지 들어갈 수 있다고 했으므로 해당 자료를 담을 수 있게 dp테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍 진행 (보텀업)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 나뉘어 떨어지는 경우와 비교해 가장 작은 값을 dp테이블에 저장
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    
print(d[x])