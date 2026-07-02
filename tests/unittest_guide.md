# Python unittest 单元测试库使用文档

## 简介

`unittest` 是 Python 内置的单元测试框架，灵感来自 Java 的 JUnit。它支持测试自动化、共享测试的设置和关闭代码、将测试聚合到集合中以及测试与报告框架的独立性。

## 快速开始

### 基础示例

```python
import unittest


def add(a, b):
    return a + b


class TestMathOperations(unittest.TestCase):
    """测试数学运算"""

    def test_add_positive_numbers(self):
        """测试正数相加"""
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        """测试负数相加"""
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        """测试加零"""
        self.assertEqual(add(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
```

### 运行测试

```bash
# 运行单个测试文件
python -m unittest test_file.py

# 运行测试类中的某个测试方法
python -m unittest test_file.TestMathOperations.test_add

# 自动发现并运行所有测试
python -m unittest discover

# 详细输出模式
python -m unittest -v test_file.py
```

---

## 核心概念

### TestCase（测试用例）

`unittest.TestCase` 是最基本的测试单元。每个测试方法必须以 `test_` 开头。

```python
class MyTestCase(unittest.TestCase):
    def test_something(self):
        """测试方法必须以 test_ 开头"""
        self.assertEqual(1 + 1, 2)
```

### TestSuite（测试套件）

用于组织多个测试用例一起运行。

```python
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMathOperations('test_add_positive_numbers'))
    suite.addTest(TestMathOperations('test_add_negative_numbers'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

### TestRunner（测试运行器）

控制测试的执行和输出。

```python
# 自定义运行器
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite())
```

### TestFixture（测试夹具）

用于准备测试环境和清理。

```python
class DatabaseTest(unittest.TestCase):
    def setUp(self):
        """每个测试方法运行前执行"""
        print("准备测试数据...")
        self.test_data = {"name": "test", "value": 123}

    def tearDown(self):
        """每个测试方法运行后执行"""
        print("清理测试数据...")
        self.test_data = None

    @classmethod
    def setUpClass(cls):
        """整个测试类运行前执行一次"""
        print("连接数据库...")

    @classmethod
    def tearDownClass(cls):
        """整个测试类运行后执行一次"""
        print("关闭数据库连接...")
```

执行顺序：
1. `setUpClass()`
2. `setUp()`
3. `test_method()`
4. `tearDown()`
5. `tearDownClass()`

---

## 断言方法（Assertions）

### 常用断言

| 方法 | 作用 |
|------|------|
| `assertEqual(a, b)` | 检查 a == b |
| `assertNotEqual(a, b)` | 检查 a != b |
| `assertTrue(x)` | 检查 x 为 True |
| `assertFalse(x)` | 检查 x 为 False |
| `assertIs(a, b)` | 检查 a is b |
| `assertIsNot(a, b)` | 检查 a is not b |
| `assertIsNone(x)` | 检查 x 为 None |
| `assertIsNotNone(x)` | 检查 x 不为 None |
| `assertIn(a, b)` | 检查 a in b |
| `assertNotIn(a, b)` | 检查 a not in b |
| `assertIsInstance(a, b)` | 检查 isinstance(a, b) |
| `assertNotIsInstance(a, b)` | 检查 not isinstance(a, b) |

### 数值比较断言

```python
class TestNumbers(unittest.TestCase):
    def test_comparisons(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)
        self.assertGreater(5, 3)
        self.assertGreaterEqual(5, 5)
        self.assertLess(3, 5)
        self.assertLessEqual(5, 5)
```

### 集合断言

```python
class TestCollections(unittest.TestCase):
    def test_list(self):
        self.assertListEqual([1, 2], [1, 2])
        self.assertCountEqual([1, 2, 1], [1, 1, 2])  # 忽略顺序

    def test_dict(self):
        self.assertDictEqual({"a": 1}, {"a": 1})

    def test_tuple(self):
        self.assertTupleEqual((1, 2), (1, 2))
```

### 异常断言

```python
class TestExceptions(unittest.TestCase):
    def test_raises(self):
        with self.assertRaises(ValueError):
            int("abc")

    def test_raises_with_message(self):
        with self.assertRaisesRegex(ValueError, "invalid literal"):
            int("abc")
```

---

## 跳过测试

```python
class TestSkipExample(unittest.TestCase):
    @unittest.skip("直接跳过此测试")
    def test_skip(self):
        self.fail("不会执行到这里")

    @unittest.skipIf(1 < 2, "条件为真时跳过")
    def test_skip_if(self):
        self.fail("不会执行到这里")

    @unittest.skipUnless(1 > 2, "条件为假时跳过")
    def test_skip_unless(self):
        self.fail("不会执行到这里")

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1, 0)  # 预期失败，不计入失败计数
```

---

## 测试目录结构

推荐的项目测试结构：

```
project/
├── stum/                    # 主包
│   ├── __init__.py
│   ├── config.py
│   ├── progress.py
│   ├── installer.py
│   └── launcher.py
├── tests/                   # 测试目录
│   ├── __init__.py
│   ├── test_config.py       # 测试配置模块
│   ├── test_progress.py     # 测试进度模块
│   ├── test_installer.py    # 测试安装模块
│   └── test_launcher.py     # 测试启动模块
└── main.py                  # 主入口
```

---

## 完整示例：测试 stum 项目

### tests/test_config.py

```python
import unittest
from stum.config import (
    MINECRAFT_PATH,
    MINECRAFT_VERSION,
    build_jvm_args,
    build_launch_options,
    update_minecraft_path,
    update_minecraft_version
)


class TestConfig(unittest.TestCase):
    """测试配置模块"""

    def test_build_jvm_args_returns_list(self):
        """测试build_jvm_args返回列表"""
        result = build_jvm_args()
        self.assertIsInstance(result, list)

    def test_build_jvm_args_contains_memory_settings(self):
        """测试JVM参数包含内存设置"""
        result = build_jvm_args()
        self.assertTrue(any('-Xmx' in arg for arg in result))
        self.assertTrue(any('-Xms' in arg for arg in result))

    def test_build_launch_options_has_required_keys(self):
        """测试启动选项包含必要字段"""
        options = build_launch_options()
        required_keys = ['username', 'uuid', 'token', 'jvm_args', 'launcher_name']
        for key in required_keys:
            self.assertIn(key, options)

    def test_update_minecraft_path(self):
        """测试更新Minecraft路径"""
        original = MINECRAFT_PATH
        update_minecraft_path('/new/path')
        self.assertEqual(MINECRAFT_PATH, '/new/path')
        update_minecraft_path(original)  # 恢复原值
```

### tests/test_progress.py

```python
import unittest
from stum.progress import get_callback


class TestProgress(unittest.TestCase):
    """测试进度显示模块"""

    def test_get_callback_returns_dict(self):
        """测试get_callback返回字典"""
        callback = get_callback()
        self.assertIsInstance(callback, dict)

    def test_get_callback_has_required_keys(self):
        """测试回调字典包含必要字段"""
        callback = get_callback()
        required_keys = ['setStatus', 'setProgress', 'setMax']
        for key in required_keys:
            self.assertIn(key, callback)

    def test_callback_functions_are_callable(self):
        """测试回调函数可调用"""
        callback = get_callback()
        for func in callback.values():
            self.assertTrue(callable(func))
```

---

## 高级用法

### Mock 模拟对象

```python
from unittest.mock import Mock, patch


class TestWithMock(unittest.TestCase):
    @patch('stum.installer.mclib')
    def test_install_with_mock(self, mock_mclib):
        """使用Mock模拟外部库"""
        mock_mclib.install.install_minecraft_version.return_value = None
        # 测试安装逻辑...

    def test_with_mock_object(self):
        """创建Mock对象"""
        mock_obj = Mock()
        mock_obj.some_method.return_value = 42
        result = mock_obj.some_method()
        self.assertEqual(result, 42)
        mock_obj.some_method.assert_called_once()
```

### 参数化测试

```python
class TestParameterized(unittest.TestCase):
    def test_multiple_cases(self):
        test_cases = [
            (1, 2, 3),
            (0, 0, 0),
            (-1, 1, 0),
            (100, 200, 300),
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)
```

### 超时控制

```python
import time


class TestTimeout(unittest.TestCase):
    def test_with_timeout(self):
        """长时间运行的测试设置超时"""
        start = time.time()
        # 执行测试...
        elapsed = time.time() - start
        self.assertLess(elapsed, 5)  # 不超过5秒
```

---

## 命令行选项

```bash
# 基本用法
python -m unittest test_module          # 测试模块
python -m unittest module.ClassName     # 测试类
python -m unittest module.ClassName.test_method  # 测试方法

# 常用选项
python -m unittest -v                   # 详细输出
python -m unittest -q                   # 安静模式
python -m unittest -f                   # 首次失败即停止
python -m unittest -c                   # 显示颜色输出
python -m unittest discover             # 自动发现测试
python -m unittest discover -s tests    # 指定测试目录
python -m unittest discover -p "*.py"   # 指定文件模式
```

## 最佳实践

1. **测试文件命名** - 以 `test_` 开头，如 `test_config.py`
2. **测试方法命名** - 以 `test_` 开头，用下划线分隔，如 `test_build_jvm_args_returns_list`
3. **每个测试只测试一个功能点** - 保持测试单一职责
4. **使用有意义的断言消息** - 方便定位问题
5. **测试前准备，测试后清理** - 使用 `setUp()` 和 `tearDown()`
6. **保持测试独立** - 测试之间不应相互依赖
7. **测试边界条件** - 空值、最大值、最小值等
8. **定期运行测试** - 确保代码质量
9. **测试覆盖率** - 尽量覆盖所有代码路径
10. **测试也要维护** - 代码重构时同步更新测试