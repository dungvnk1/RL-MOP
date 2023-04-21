# Q-learning  

- Giới thiệu về Q-learning: 
  + Q-learning là một thuật toán học tăng cường (Reinforcement Learning) được sử dụng để giải quyết các bài toán liên quan đến việc ra quyết định trong một môi trường không biết trước.
  + Thuật toán này hoạt động dựa trên việc xác định giá trị của các hành động trong một trạng thái cụ thể, được gọi là giá trị Q. Giá trị Q của một hành động được tính toán dựa trên tổng điểm thưởng (reward) thu được từ các hành động tiếp theo và giá trị Q của trạng thái đó.

- Bảng Q-table:
  + Bảng Q-table là một cách để lưu trữ các giá trị Q cho mỗi trạng thái và hành động có thể được thực hiện trong trạng thái đó.
  + Khi áp dụng Q-learning, thuật toán sẽ cập nhật các giá trị trong bảng Q-table dựa trên kết quả của các hành động được thực hiện trong môi trường.

- Khám phá/ Khai thác (Exploration/ Exploitation):
  + Trong Q-learning, khám phá (Exploration) và Khai thác (Exploitation) là hai khái niệm quan trọng để cân bằng giữa việc tìm kiếm các hành động mới và sử dụng những hành động đã biết để đạt được điểm thưởng (reward) cao nhất.
  + Exploration được sử dụng để tìm kiếm và thu thập thông tin về các hành động mới và trạng thái mới trong môi trường, trong khi Exploitation được sử dụng để thực hiện các hành động được biết là đạt được điểm thưởng cao nhất đã thu thập cho đến nay.
  + Sự cân bằng giữa Khám phá và Khai thác là rất quan trọng trong RL. Nếu một tác nhân tập trung quá nhiều vào Khám phá, nó có thể không thể tìm ra chính sách tối ưu vì nó dành quá nhiều thời gian thu thập thông tin. Ngược lại, nếu một tác nhân tập trung quá nhiều vào Khai thác, nó có thể bị mắc kẹt trong một chính sách không tối ưu vì nó không thu thập đủ thông tin về môi trường.
 
- Reward function: 
  + Reward function (hàm phần thưởng) là một thành phần quan trọng trong học tăng cường. Nó định nghĩa mức độ thưởng hoặc phạt cho mỗi hành động mà tác nhân thực hiện trong môi trường. Mục đích của học tăng cường là tìm ra một chính sách hành động sao cho tổng phần thưởng thu được là lớn nhất
  + Hàm phần thưởng có thể được định nghĩa theo nhiều cách khác nhau tùy thuộc vào bài toán cụ thể. Ví dụ, trong trò chơi điều khiển xe đua, hàm phần thưởng có thể cho phép tác nhân nhận được điểm thưởng khi vượt qua một chướng ngại vật và bị phạt khi va chạm với chướng ngại vật hoặc rời khỏi đường đua.

- Ví dụ về Q-learning: 
  + Một ví dụ về Q-learning là việc huấn luyện một con robot để di chuyển từ điểm xuất phát đến đích trong một mê cung.
  + Robot sẽ phải tìm kiếm các đường đi mới thông qua Khám phá, và sử dụng các đường đi đã biết thông qua Khai thác để đạt được điểm thưởng cao nhất. Hàm reward có thể được định nghĩa dựa trên khoảng cách đến đích và số lượng các rào cản đã vượt qua.
  ![image](https://user-images.githubusercontent.com/126397851/233561084-89e78c3f-0eed-4dc9-b89c-f9646ee159d8.png)
