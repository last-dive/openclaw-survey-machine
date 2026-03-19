# 使用示例

## 基础用法

```bash
./survey-machine.sh "无人机通信时延"
```

## 指定子主题

```bash
./survey-machine.sh -t "无人机通信时延" -s "时延辨识,预测补偿,制导控制"
```

## 完整定制

```bash
./survey-machine.sh \
    -t "强化学习飞行控制" \
    -s "多旋翼,固定翼,VTOL" \
    -p 60
```

## 自然语言触发

```
帮我写一篇关于无人机通信时延的综述
```
