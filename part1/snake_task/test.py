import sys
import unittest
from pathlib import Path
import os
import main

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[: basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402


class ExceptionTestCase(SkyproTestCase):
    def test_init_returns_class_instances(self):
        func_name = "snake_checker"
        func = getattr(main, func_name)

        self.assertTrue(
            func,
            f"%@Проверьте, что функция {func_name} определена в модуле."
        )

        result = func("yeah! python is awesome ")
        self.assertIsInstance(
            result, bool,
            "%@Проверьте, что функция возвращает результат типа boolean."
        )

        self.assertTrue(
            result,
            "%@Проверьте, что если на вход ваша функция получает строку со словом python, то она возвращает True."
        )

        result = func("py py is on")
        self.assertFalse(
            result,
            "%@Проверьте, что если на вход ваша функция получает строку, не содержащую слово python,"
            " то она возвращает False."
        )


if __name__ == "__main__":
    unittest.main()
