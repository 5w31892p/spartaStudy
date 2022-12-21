package cafe.presentation;

import cafe.menu.Menu;
import cafe.menu.MenuItem;

// UI
public class MenuInterFace {
    public MenuInterFace(Menu menu) {
        System.out.println("=============== 메뉴 목록 ===============");
        for (MenuItem menuItem : menu.getMenuItemsList()) {
            System.out.println("메뉴 이름 : " + menuItem.getName() + ", 가격 : " + menuItem.getPrice());
        }
    }
}
