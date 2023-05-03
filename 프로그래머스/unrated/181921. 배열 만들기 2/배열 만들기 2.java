import java.util.Arrays;

class Solution {
     public static boolean filter(int num) {
        int extra;
        while (num > 0) {
            extra = num % 10; // 맨 뒷자리
            if (extra % 5 != 0)  // 5로 나눠진다는것 -> 끝자리가 0이 된다는 조건은 함께 충족
                {
                return false;
            }
          num /= 10;  
        }
        return true;
    }
    
    public int[] solution(int l, int r) {
        int[] answer = new int[r];
        int cnt = 0;
        for (int i = l; i <= r; i++) {
            if (filter(i)) {
                answer[cnt] = i;
                cnt=cnt+1;
            }
        }
        answer = Arrays.stream(answer)
                .filter(i -> i != 0)
                .toArray();

        if (answer.length == 0) {
            int[] res = {-1};
            return res;
        }
        return answer;
    }
}