import gym
import numpy as np
import matplotlib.pyplot as plt

class TSPEnv(gym.Env):
    def __init__(self, n_cities=10):                                #Khởi tạo lớp TSPEnv với số lượng thành phố là n_cities
        super(TSPEnv, self).__init__()
        self.n_cities = n_cities
        self.distances = np.random.rand(n_cities, n_cities)         #Ma trận khoảng cách giữa các thành phố 
        self.current_city = 0       
        self.visited_cities = [0]                                   #Danh sách thành phố đã ghé thăm
        self.observation_space = gym.spaces.Discrete(n_cities)      
        self.action_space = gym.spaces.Discrete(n_cities)           #2 dòng này định nghĩa không gian quan sát và không gian hành động cho môi trường
        
    def reset(self):                                                #Đưa môi trường về trạng thái ban đầu, đặt lại vị trí của thành phố hiện tại và danh sách các thành phố đã được ghé thăm và trả về vị trí của thành phố hiện tại 
        self.current_city = 0
        self.visited_cities = [0]
        return self.current_city
    
    def step(self, action):                                         
        reward = -self.distances[self.current_city][action]         #Tính toán phần thưởng (reward) bằng cách lấy âm giá trị của khoảng cách giữa thành phố hiện tại và thành phố được chọn để đi 
        self.current_city = action                                  #Cập nhật thành phố hiện tại thành thành phố được chọn để đi 
        self.visited_cities.append(action)                          #Thêm thành phố được chọn vào danh sách các thành phố đã được ghé thăm
        if len(self.visited_cities) == self.n_cities:               #Nếu đã đi hết tất cả các thành phố, thì trạng thái kết thúc (done) được đặt là True và phần thưởng (reward) được trừ thêm giá trị của khoảng cách giữa thành phố được chọn để đi và thành phố xuất phát (self.distances[action][0]). Ngược lại, nếu chưa đi hết tất cả các thành phố, thì trạng thái kết thúc là False.
            done = True
            reward -= self.distances[action][0]
        else:
            done = False
        return self.current_city, reward, done, {}                  #Trả về vị trí của thành phố hiện tại, phần thưởng, trạng thái kết thúc và thông tin bổ sung dưới dạng một từ điển trống.

class TSPAgent:
    def __init__(self, env):                                        #Khởi tạo bảng Q-table rỗng cùng các tham số RL
        self.q_table = np.zeros((env.observation_space.n, env.action_space.n))  
        self.env = env
        self.epsilon = 1.0
        self.epsilon_decay = 0.9999
        self.alpha = 0.5
        self.gamma = 0.99
        
    def choose_action(self, state):                                 #Nếu giá trị ngẫu nhiên được sinh ra nhỏ hơn giá trị epsilon thì một hành động ngẫu nhiên sẽ được chọn (thực hiện khám phá). Ngược lại, giá trị của bảng Q sẽ được tra cứu để chọn hành động cho phần còn lại của chính sách tối ưu của agent.
        if np.random.uniform() < self.epsilon:
            return self.env.action_space.sample()
        else:
            return np.argmax(self.q_table[state])
        
    def update_q_table(self, state, action, reward, next_state):    #Công thức trong Q-learning được sử dụng để tính giá trị Q tại trạng thái hiện tại và hành động tương ứng sẽ được cập nhật với giá trị mới được tính bằng tỉ lệ trọng số giữa giá trị cũ và giá trị mới. Giá trị mới này được tính bằng cộng phần thưởng hiện tại và phần thưởng dự báo cho trạng thái tiếp theo, được tính dựa trên giá trị lớn nhất của bảng Q tại trạng thái tiếp theo.
        self.q_table[state][action] = (1 - self.alpha) * self.q_table[state][action] + \
                                       self.alpha * (reward + self.gamma * np.max(self.q_table[next_state]))
    
    def train(self, n_episodes=10000):                              #Hàm train được sử dụng để huấn luyện agent. 
        rewards = []
        for episode in range(n_episodes):                           #Agent sẽ được huấn luyện trong một số lượng episodes nhất định.
            state = self.env.reset()
            done = False
            episode_reward = 0
            while not done:                                         #Với mỗi episode, agent sẽ được khởi tạo lại trạng thái và thực hiện các hành động cho đến khi trạng thái kết thúc.
                action = self.choose_action(state)
                next_state, reward, done, _ = self.env.step(action)
                episode_reward += reward
                self.update_q_table(state, action, reward, next_state)
                state = next_state
            self.epsilon *= self.epsilon_decay                      #Mỗi lần hoàn thành một episode, epsilon sẽ được giảm dần theo hàm mũ với giá trị epsilon_decay nhằm giảm sự khám phá ngẫu nhiên theo thời gian.
            rewards.append(episode_reward)
        return rewards

#Gọi các biến và hàm để chạy chương trình
env = TSPEnv()
agent = TSPAgent(env)
def plot_rewards(rewards):
    plt.plot(rewards)
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.title('Reward per Episode')
    plt.show()

rewards = agent.train(n_episodes=10000)
plot_rewards(rewards)


