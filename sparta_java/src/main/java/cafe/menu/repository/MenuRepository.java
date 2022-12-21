package cafe.menu.repository;

import cafe.menu.Menu;
import cafe.menu.MenuItem;

public interface MenuRepository {
    void saveMenu(Menu menu);
    MenuItem getMenuItem(int menuid, String menuName);
    // getmenuitem 하나하나가 id가 있을 수 있으니까 menuid로
    // 명시적으로 MenuItem을 품고 있기 때문에 의도 전달을 잘 하기 위해 menuid로
    Menu getMenu(int id); // getmenu니까 id
}
