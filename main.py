import approximation
import numpy as np

if __name__ == "__main__":

    # points = set()
    # print("Введите точки. Чтобы подтвердить выбор - нажмите Enter. Чтобы закончить ввод нажмите Enter ещё раз")
    # while True:
    #     try:
    #         source = input().strip()
    #         if len(source) == 0:
    #             if len(points) < 3:
    #                 print("Введите хотя бы 3 различных точки")
    #                 continue
    #             else:
    #                 break
    #         pair = source.split(" ")
    #         if len(pair) != 2:
    #             print("Введите два числа")
    #             continue
    #         pair[0] = float(pair[0])
    #         pair[1] = float(pair[1])
    #         points.add((pair[0], pair[1]))
    #     except ValueError:
    #         print("Не удалось распознать числа. Попробуйте ещё раз")
    print(
        "Выберите функцию для апроксимации:\n1. ax+b\n2. ax^2+bx+c\n3. ae^(bx)\n4. alog(x)+b\n5. ax^b\nВведите число от 1 до 5")
    while True:
        try:
            f_type = int(input().strip())
            if f_type > 5 or f_type < 1:
                print("Введите число от 1 до 5")
                continue
            break
        except ValueError:
            print("Неверный формат числа. Введите число от 1 до 5")
    points = [(0.2, 1.25), (0.8, 1.41), (1.4, 1.59), (2, 1.82), (2.6, 2.13), (3.2, 2.27), (3.8, 2.56), (4.4, 2.89),
              (5, 3.27), (5.6, 3.69), (6.2, 4.15), (6.8, 4.54), (7.4, 5.31)]
    points = np.array(list(points))

    lq = approximation.LeastSquares(f_type - 1, points[:, 0], points[:, 1])
    try:
        lq.calc_coefs()
        try:
            lq.recalc_coefs()
        except Exception as inst:
            print(inst.args[0])
        lq.draw_graphics()
    except Exception as inst:
        print(inst.args[0])
