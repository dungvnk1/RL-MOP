# Reinforcement Learning

- Markov Decision Processes: 
  + Là quá trình đươc gọi là một "thời gian quá trình kiểm soát ngẫu nhiên rời rạc"
  + Một MDPs bao gồm states, tập hợp actions trong mỗi states, tập hợp các xác suất xác định states tiếp theo và rewards được trả về sau mỗi action.
  + Xác suất agent chuyển sang state mới chỉ phụ thuộc state, action hiện tại, không phụ thuộc yếu tố trước đó. 
  + MDP được sử dụng trong nhiều lĩnh vực: AI, robotics, ... 
 
- Policy:
  + Là hàm ánh xạ states sang actions. Xác định hành vi của agent trong environment. Mục tiêu của agent là học policy tối ưu để tối đa hóa rewards tích lũy được theo thời gian.
  + Determistic Policy: ánh xạ trực tiếp state sang action, cho trước một state và policy sẽ chọn action tương ứng.
  + Stochastic Policy: chọn action dựa trên phân bố xác suất, chọn actions khác nhau cho cùng 1 state khi khởi chạy.
  + Agent trong RL học policy tối ưu thông qua việc thử và sai được lặp lại liên tục. Khám phá environment bằng actions và nhận rewards. Cập nhật policy dựa trên rewards để cải thiện reward tích lũy theo thời gian. Khi agent + policy tối ưu -> tối đa hóa reward tích lũy được theo dự kiến thì quá trình học kết thúc.

- Value Function: 
  + Dùng để đánh giá, so sánh mặt tốt của actions trong một state. 
  + VF đại diện tổng reward kì vọng(bắt đầu từ một state+action+policy cụ thể).
  + Được ước tính bằng các pp lặp như DP.
  + State-value function: ước tính giá trị một state cụ thể.
  + Action-value function: ước tính giá trị một action cụ thể trong một state cụ thể.
  + Optimal-value function: cung cấp tổng reward kỳ vọng lớn nhất(agent cố gắng học).

- Example: 
  + Robotics: RL được sử dụng để dạy agents thực hiện đa tác vụ: gắp vật thể, đi dạo, lái drones. Thuật toán DQN dùng deep neural network để ước tính action-value function -> dạy agent vượt mê cung và cầm vật thể.
