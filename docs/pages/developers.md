# للمطورين (For Developers)

يحتوي المشروع على أدوات برمجية (Python) لأتمتة العملية، لكنها **غير ضرورية** للمساهمة في التقييم.

### الأدوات المتاحة

#### 1. تحويل البيانات

يوجد سكربت في `scripts/convert_csv_to_excel.py` لتحويل ملف الـ CSV إلى Excel ليسهل ملؤه يدوياً.

```bash
python scripts/convert_csv_to_excel.py
```

#### 2. التقييم البرمجي

يوجد مثال في `examples/basic_evaluation.py` لاستدعاء APIs النماذج (OpenAI, Anthropic, etc) مباشرة لتقييم جملة معينة من القائمة.

كما يوجد `examples/evaluation_notebook.ipynb` لتجربة تفاعلية.

### التثبيت

```bash
pip install -r requirements.txt
```
