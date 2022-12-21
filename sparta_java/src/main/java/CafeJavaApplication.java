import cafe.menu.JavaMenuService;
import cafe.menu.Menu;
import cafe.menu.MenuItem;
import cafe.menu.MenuService;
import cafe.presentation.MenuInterFace;
import cafe.presentation.UserInterFace;

import java.util.Scanner;

public class CafeJavaApplication {

    public static void main(String[] args) {
        UserInterFace UI = new UserInterFace();
        UI.run(); // web-browser

//        System.out.println("=============== 입력 ( 1번 ) 메뉴 생성 ===============");
//        System.out.println("============= 입력 ( 2번 ) 메뉴 목록 조회 =============");
//        System.out.println("=============== 입력 ( q ) 시스템 종료 ===============");
//         여기다가 No No!!


        // application-tier
        MenuService menuService = new JavaMenuService();

        // 1 누르고 꺼져서 while문 안에 넣음
        while (true) {
            Scanner input = new Scanner(System.in);
            String fristInput = input.nextLine(); // next는 스페이스 치면 끊어버리고, nextLine은 엔터치면 끊어버림
            if (fristInput.equals("1")) {
                menuService.createMenu();
            } else if (fristInput.equals("2")) {
                Menu menu = menuService.getMenu(1);
                new MenuInterFace(menu);
                Scanner menuNameInput = new Scanner(System.in);
                String menuName = menuNameInput.nextLine();

                System.out.println("입력 받은 메뉴 이름 : " + menuName);
                MenuItem menuItem = menuService.getMenuItem(1, menuName);
                System.out.println("메뉴 이름 : " + menuItem.getName());

            } else if (fristInput.equals("q")) {
                System.out.println("시스템 종료");
                System.exit(0);
            }
        }

//        Menu menu = new Menu(); // 메뉴 만들어진다.
//        MenuItem menuItem = menu.getMenuItem("아메리카노");
//        MenuRepository menuRepository = new JavaMenuRepository();

//        JavaMenuRepository menuRepository = new JavaMenuRepository(); 잘 만들어 놓고 앞에 JavaMenuRepository 붙이게되면 new JavaMenuRepository(); 자리에 new SpringMenuRepository(); 못들어감

//        menuRepository.saveMenu(menu);
//        menuRepository.saveMenu(menu);
//        menuRepository.saveMenu(menu);
//        System.out.println(menuRepository.getMenu(1).getMenuItem("아메리카노").getName());

    }
}
