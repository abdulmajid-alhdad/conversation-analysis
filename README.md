# محرك تحليل المحادثات العربية

مشروع لبناء نظام لتحليل المحادثات العربية بطريقة قابلة للتفسير والتتبع ومدعومة بالأدلة.

الحالة الحالية:
M0 - IMPLEMENTATION READINESS

المشروع حاليا في مرحلة تجهيز بيئة التنفيذ والبنية الهندسية الأساسية.
لم يبدأ تنفيذ منطق تحليل المحادثات بعد.

## بيئة Python

نسخة Python المطلوبة:
CPython >=3.13,<3.14

النسخة الحالية:
CPython 3.13.15

النسخة الأساسية يديرها uv.

تحديد Python الأساسي:
$BASE_PY = (uv python find 3.13).Trim()

لا يجوز تثبيت مكتبات المشروع داخل Python الأساسي المشترك.

ممنوع استخدام:
--break-system-packages
--system-site-packages

## بيئة المشروع المعزولة

مسار البيئة الحالية:
D:\python-envs\conversation-analysis

مفسر المشروع:
D:\python-envs\conversation-analysis\Scripts\python.exe

مجلد المشروع:
D:\project\conversation-analysis

لا نستخدم بيئة Python داخل المستودع مثل:
.venv
venv
env

تفعيل البيئة ليس إلزاميا.
الأوامر الرسمية تستخدم مفسر المشروع مباشرة.

## عزل البيئة

يجب أن يتحقق:
sys.prefix != sys.base_prefix

ويجب أن تكون:
include-system-site-packages = false

هذا يمنع المشروع من الاعتماد على مكتبات Python المشتركة مع مشاريع أخرى.

## إدارة الحزم

الملف المرجعي:
pyproject.toml

مدير التثبيت الأساسي:
pip

Build Backend:
setuptools.build_meta

أدوات التطوير الحالية:
pytest
ruff
mypy

سياسة إعداد البيئة:
Verify and Reuse First

أي يتم التحقق من الأدوات والملفات الموجودة محليا قبل تنزيل أي شيء جديد.

## Editable Installation

المشروع مثبت حاليا بصيغة Editable.

Distribution:
arabic-conversation-analysis

Import Package:
conversation_analysis

الموقع:
D:\project\conversation-analysis

وهذا يسمح بأن تشير الحزمة مباشرة إلى ملفات src دون الحاجة إلى إعادة تثبيتها بعد كل تعديل.

## تشغيل المشروع

الأمر:
& $PROJECT_PY -m conversation_analysis

الناتج الحالي المتوقع:
conversation-analysis: M0 bootstrap

هذه نقطة تشغيل Bootstrap فقط ولا تحتوي على Business Logic.

## بنية المشروع

المجلدات الأساسية:

src/conversation_analysis/core
src/conversation_analysis/application
src/conversation_analysis/delivery
src/conversation_analysis/infrastructure

tests/unit
tests/architecture
tests/conformance
tests/integration
tests/e2e
tests/support

fixtures/sources
fixtures/canonical
fixtures/analysis
fixtures/evaluation

docs/adr

## حدود الطبقات المعمارية

core:
لا يجوز أن تعتمد على application أو delivery أو infrastructure.

application:
يمكنها الاعتماد على core.

delivery:
يمكنها الاعتماد على application و core contracts عند وجود مبرر.

infrastructure:
يمكنها الاعتماد على application ports و core contracts.

ويجب أن يبقى Dependency Graph الخاص بـ Core بلا Cycles.

## الاختبارات

تشغيل الاختبارات:
& $PROJECT_PY -m pytest

التصنيفات:
tests/unit
tests/architecture
tests/conformance
tests/integration
tests/e2e

tests/support مخصص للبنية المساعدة للاختبارات فقط.

## Fixtures

مجموعات Fixtures:

fixtures/sources
fixtures/canonical
fixtures/analysis
fixtures/evaluation

يجب أن تكون بيانات الاختبار اصطناعية أو مكتوبة يدويا أو مجهولة الهوية بشكل مناسب.

المحادثات الشخصية الخام لا يجوز إدخالها إلى Git.

## Fixture Loader

الـ Fixture Loader الحالي مسؤول فقط عن:

- تحديد مسار Fixture.
- قراءة نص UTF-8.
- قراءة expected JSON.
- الفشل الصريح عند غياب الملفات.

ولا يقوم بأي:

Parsing
Canonicalization
Analysis
Semantic Processing
Domain Interpretation

## فحص الجودة المحلي

بوابة الجودة المحلية تتكون من:

1. Ruff formatting
2. Ruff linting
3. mypy strict
4. pytest

الأوامر:

& $PROJECT_PY -m ruff format --check src tests
& $PROJECT_PY -m ruff check src tests
& $PROJECT_PY -m mypy src/conversation_analysis
& $PROJECT_PY -m pytest

يجب أن تنجح جميعها قبل إغلاق M0.

## Architecture Decision Records

قرارات المعمارية موجودة في:
docs/adr

ترتيب السلطة:

Project Charter
ثم Adopted Specialized Specifications
ثم ADRs
ثم Implementation

لا يجوز لقرار ADR أن يخالف عقدا أعلى منه بصورة صامتة.

## Git و GitHub

نظام التحكم بالإصدارات:
Git

الفرع الأساسي:
main

قبل إغلاق M0 يجب أن يوجد:

GitHub Repository خاص PRIVATE
Remote باسم origin
Initial Push

GitHub Actions مؤجلة حاليا.

## حماية المستودع

لا يجوز رفع:

- كلمات المرور.
- Tokens.
- Secrets.
- Credentials المحلية.
- المحادثات الشخصية الخام.
- محتويات بيئة Python.
- الإعدادات السرية المحلية.

ولا يتم تجاهل مجلد .vscode بالكامل بشكل تلقائي.

## حدود M0

M0 لا تنفذ حاليا:

- Source Ingestion
- WhatsApp Parsing
- Canonicalization
- Conversation Analysis
- Semantic Processing
- LLM Integration
- Embeddings
- Vector Search
- Evidence Reasoning
- Production Persistence

هدف M0 هو إنشاء أساس هندسي ثابت وقابل للاختبار قبل بدء تنفيذ قدرات النظام الفعلية.