import sys
import unittest
from pathlib import Path
import os
import main
import solution

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[: basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402


class ExceptionTestCase(SkyproTestCase):
    def setUp(self):
        self.expected = solution.greeting.__annotations__
        self.annotations = main.greeting.__annotations__

    def test_func_has_annotations(self):
        for annotation in self.expected:
            if annotation != "return":
                self.assertIn(
                    annotation, self.annotations,
                    f"%@Проверьте что написали аннотацию для аргумента {annotation}"
                )
            else:
                self.assertIn(
                    annotation, self.annotations,
                    f"%@Проверьте что Вы написали аннотацию на значение, которое возвращается функцией"
                )

        for annotation in self.expected:
            if annotation != "return":
                self.assertEqual(
                    self.annotations.get(annotation), self.expected.get(annotation),
                    f"%@Проверьте что правильно определили тип для аргумента {annotation}"
                )
            else:
                self.assertEqual(
                    self.annotations.get(annotation), self.expected.get(annotation),
                    f"%@Проверьте, что правильно написали тип данных, которые возвращает функция"
                )


if __name__ == "__main__":
    unittest.main()
