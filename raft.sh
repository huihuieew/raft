python3 raft.py \
  --datapath data/RAFT.pdf \
  --output outputs \
  --output-format hf \ # or completion or chat
  --distractors 3 \
  --p 1.0 \
  --doctype pdf \
  --chunk_size 512 \
  --questions 2 \
  --system-prompt-key llama \
  --embedding_model doubao-embedding-large-text-250515 \
  --completion_model deepseek-r1-250120 \

# --embedding_model text-embedding-v2 \
# --completion_model qwen-plus \
# --openai_key f40416fd-bfd1-4370-b74f-15c3338d0c58
# --openai_key sk-f48122216ef34a308d4da05e4fa4c89a  ali apikey

python raft.py --datapath data/RAFT.pdf --output outputs --output-format hf --distractors 3 --p 1.0 --doctype pdf --chunk_size 512 --questions 2 --completion_model qwen-plus --openai_key sk-f48122216ef34a308d4da05e4fa4c89a
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test --output-format hf --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model qwen-plus --openai_key sk-f48122216ef34a308d4da05e4fa4c89a
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test01 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test02 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key llama
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test03 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 5 --completion_model deepseek-r1-250120 --system-prompt-key deepseek
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test04 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 5 --completion_model deepseek-r1-250120 --system-prompt-key deepseek
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test05 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 5 --completion_model deepseek-r1-250120 --system-prompt-key deepseek
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test06 --output-format completion --distractors 4 --p 1.0 --doctype txt --chunk_size 512 --questions 5 --completion_model deepseek-r1-250120 --system-prompt-key deepseek
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test07 --output-format completion --distractors 4 --p 1.0 --doctype txt --chunk_size 512 --questions 5 --completion_model deepseek-r1-250120 --system-prompt-key deepseek
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test08 --output-format completion --distractors 4 --p 1.0 --doctype txt --chunk_size 512 --questions 3 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/“光电子学”课程的实践与思考_杨晓占_llm_correct.md --output outputs_test09 --output-format completion --distractors 4 --p 1.0 --doctype txt --chunk_size 512 --questions 5 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/“半导体光电子学”双语教学探讨_贾宏志_llm_correct.md --output outputs_test10 --output-format completion --distractors 4 --p 1.0 --doctype txt --chunk_size 512 --questions 1 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/“光电子学”课程的实践与思考_杨晓占_llm_correct.md --output outputs_test09 --output-format completion --distractors 4 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test08 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/“基于低温多晶硅TFT基板...ED关键技术研发”通过验收_llm_correct.md --output outputs_test11 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/“战略性先进电子材料”重点...印刷TFT材料与器件的研究_张小涛_llm_correct.md --output outputs_test12 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/“显示技术”网络课程的设计与开发_况亚伟_llm_correct.md --output outputs_test13 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/“液晶显示器件物理专业方向”的实验设置_张志东_llm_correct.md --output outputs_test14 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/“有机发光二极管（OLEDs）”专刊序_马於光_llm_correct.md --output outputs_test15 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/“战略性先进电子材料”重点...印刷TFT材料与器件的研究_张小涛_llm_correct.md --output outputs_test16 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/“自发光”平板显示未雨绸缪...战LCD的SED、OLED_陈宏林_llm_correct.md --output outputs_test17 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/《OLED模组基本额定值和特性》国际提案要点解读_来航曼_llm_correct.md --output outputs_test18 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/《透明液晶显示光学测试方法》国际提案要点解读_来航曼_llm_correct.md --output outputs_test19 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/《显示器能效限定值及能效等级》标准解析_吴蔚华_llm_correct.md --output outputs_test20 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/■面InGaN量子阱中的静...光发光二极管光电性能的影响_尹瑞梅_llm_correct.md --output outputs_test21 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/1,8-萘酰亚胺类有机小分子电致发光材料的研究进展_王启_llm_correct.md --output outputs_test22 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/2.7”a-Si_TFT矩阵(英文)_熊绍珍_llm_correct.md --output outputs_test23 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/2-对联苯-8-羟基喹啉锌...及其应用于新型白光OLED_赵婷_llm_correct.md --output outputs_test24 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/2英寸全彩色AM-OLED显示屏的驱动方案_尹盛_llm_correct.md --output outputs_test25 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/3英寸黑白a-siTFT-LCD驱动系统_孙明峰_llm_correct.md --output outputs_test26 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/5G时代新型先进显示技术发...—访中国科学院院士欧阳钟灿_张莹_llm_correct.md --output outputs_test27 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/5种液晶显示优劣谈_llm_correct.md --output outputs_test28 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/6.5万彩色显示PM-OLED控制与驱动芯片_秦波_llm_correct.md --output outputs_test29 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/7.6cm多色有源矩阵液晶显示器_冯治兴_llm_correct.md --output outputs_test30 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/8光罩BCE结构IGZO-...的钝化层通孔柱状不良的改善_刘浩_llm_correct.md --output outputs_test31 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/9.5英寸对角线的多色非晶硅TFT-LCD板_陈宏琪_llm_correct.md --output outputs_test32 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/9款38cm(15英寸)TFT_LCD显示器横向评测_张韬_llm_correct.md --output outputs_test33 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/9英寸MIM矩阵式液晶显示器件_陈树民_llm_correct.md --output outputs_test34 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/10大新显示技术_llm_correct.md --output outputs_test35 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/10万象素a-Si_TFT有源矩阵的优化技术_徐重阳_llm_correct.md --output outputs_test36 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/12.7cm彩色AM-OLED显示屏的驱动模块_张繁_llm_correct.md --output outputs_test37 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/12.7cm彩色AM-OLED显示器分场驱动研究_沈亮_llm_correct.md --output outputs_test38 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/12.9英寸高分辨率多色TFT—LCD_师庆华_llm_correct.md --output outputs_test39 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/13.8英寸高分辨率多色TFT—LCD_王阳_llm_correct.md --output outputs_test40 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/17.8cm彩色AMOLED驱动模块的研制_尹盛_llm_correct.md --output outputs_test41 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/22cm反射式彩色TFT_LCD_孙再吉_llm_correct.md --output outputs_test42 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/22英寸广色域——HP_L2245w_真水无味_llm_correct.md --output outputs_test43 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/80C196KC与液晶显示...174的接口设计及编程实现_冯占英_llm_correct.md --output outputs_test44 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/125mm彩色AMOLED的多晶硅TFT基板_孟志国_llm_correct.md --output outputs_test45 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/128×64点阵式OLED的驱动电路_董桂芳_llm_correct.md --output outputs_test46 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/200mm×200mm_OLED步进投影曝光机_周畅_llm_correct.md --output outputs_test47 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/256×64点阵液晶显示器模块_吴训_llm_correct.md --output outputs_test48 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/256级灰度OLED驱动电路_陈志明_llm_correct.md --output outputs_test49 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/400×640象素液晶显示的研制_杨兆芳_llm_correct.md --output outputs_test50 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2
python raft.py --datapath data/640×480_TFT-AMLCD有源层的制备_葛长军_llm_correct.md --output outputs_test51 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key deepseek-v2

