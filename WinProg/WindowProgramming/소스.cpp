#include <Windows.h>

#include <iostream>
#include <random>
#include <math.h>
#include <mmsyscom.h>
#include <mmsystem.h>
#include "resource.h"
#include "Digitalv.h"


#pragma comment(lib,"winmm.lib")
#pragma comment(lib, "msimg32.lib")

#define PI 3.1415926535


using namespace std;

//#pragma comment(linker,"/entry:WinMainCRTStartup /subsystem:console")
HINSTANCE g_hInst;
LPCTSTR lpszClass = L"Window Class Name";
LPCTSTR lpszWindowName = L"용사는 타이밍";
LRESULT CALLBACK WndProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
random_device rd;
default_random_engine dre(rd());
uniform_int_distribution<> uid(0, 3);
uniform_int_distribution<> puid(80, 120);
uniform_int_distribution<> buid(1, 8);
static bool AD;
int sound_sec = 0;
MCI_OPEN_PARMS mciOpen;
MCI_PLAY_PARMS mciPlay;
DWORD dwID1, dwID2, dwID3, dwID4, dwID5,dwID6;
HWND hWnd;
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpszCmdParam, int nCmdShow)
{
	
	MSG Message;
	WNDCLASSEX WndClass; 
	g_hInst = hInstance;

	WndClass.cbSize = sizeof(WndClass);
	WndClass.style = CS_HREDRAW | CS_VREDRAW;
	WndClass.lpfnWndProc = (WNDPROC)WndProc;
	WndClass.cbClsExtra = 0;
	WndClass.cbWndExtra = 0;
	WndClass.hInstance = hInstance;
	WndClass.hIcon = LoadIcon(NULL, IDI_APPLICATION);
	WndClass.hCursor = LoadCursor(NULL, IDC_ARROW);
	WndClass.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
	WndClass.lpszMenuName = NULL;
	WndClass.lpszClassName = lpszClass;
	WndClass.hIconSm = LoadIcon(NULL, IDI_APPLICATION);
	RegisterClassEx(&WndClass);

	hWnd = CreateWindow(lpszClass, lpszWindowName, WS_SYSMENU , 0, 0, 1280, 800, NULL, (HMENU)NULL, hInstance, NULL);

	ShowWindow(hWnd, nCmdShow);
	UpdateWindow(hWnd);
	while (GetMessage(&Message, 0, 0, 0)) {
		TranslateMessage(&Message);
		DispatchMessage(&Message);
	} 
	return Message.wParam;
}
enum DIRECTION {
	STOP,
	UP,
	DOWN,
	LEFT,
	RIGHT
};
struct Charactor {
	int Adirection, MJudgement, dodge, special;
	double damage, def, hp, mp, maxhp;
	int motion, stage, deadcount;
	double percent;
	POINT location;
	bool behavior, alive, just, specialon, attack, kill;
	bool cheat;
};
struct Monster {
	int damage, def, hp, pattern, maxhp;
	int type, random, Adirection;
	double percent;
	POINT location;
	bool attack, alive, stun;
};

static bool mjust = false, motion = false;
static int x = 0, y = 0;

void Cattack(Charactor* a, Monster* b)
{
	if (!mjust) {
		if (a->cheat)
			b->hp = 0;
		b->hp = b->hp - ((a->damage * puid(dre) / 100) - b->def);
		PlaySound(TEXT("blood.wav"), NULL, SND_FILENAME | SND_ASYNC);
	}
	else {
		if (a->cheat)
			b->hp = 0;
		b->hp = b->hp - 2 * (a->damage * puid(dre) / 100 - b->def);
		PlaySound(TEXT("blood.wav"), NULL, SND_FILENAME | SND_ASYNC);
	}
	b->percent = b->hp * 100 / b->maxhp;
	y = 10;
	if (b->hp <= 0) {
		b->hp = 0;
		b->alive = false;
		AD = false;
		SetTimer(hWnd, 23, 1000, NULL);
		mciOpen.lpstrElementName = TEXT("Monster_Death.mp3");
		mciSendCommand(0, MCI_OPEN, MCI_OPEN_ELEMENT | MCI_OPEN_TYPE, (DWORD)(LPVOID)& mciOpen);
		dwID6 = mciOpen.wDeviceID;
		mciSendCommand(dwID6, MCI_PLAY, MCI_NOTIFY, (DWORD)(LPVOID)& mciPlay);
		a->special = 0;
		a->stage++;
		b->stun = false;
		a->kill = true;
		if (a->deadcount == 0) {
			a->maxhp = a->maxhp * 1.1;
			a->hp = a->hp * 1.1;
			a->def = a->def * 1.1;
			a->damage = a->damage * 1.1;
		}
		else {
			a->maxhp = a->maxhp * 1.05;
			a->hp = a->hp * 1.05;
			a->def = a->def * 1.05;
			a->damage = a->damage * 1.05;
		}
		y = 40;
	}
}

void Mattack(Monster* a, Charactor* b)
{
	if (b->cheat)
		;
	else
	{
		b->hp = b->hp - ((a->damage * puid(dre) / 100) - b->def);
		b->percent = b->hp * 100 / b->maxhp;
		PlaySound(TEXT("blood.wav"), NULL, SND_FILENAME | SND_ASYNC);
	}
	y = 10;
	if (b->hp <= 0) {
		b->hp = 0;
		b->alive = false;
		SetTimer(hWnd, 23, 1000, NULL);
		mciOpen.lpstrElementName = TEXT("Char_Death.mp3");
		mciSendCommand(0, MCI_OPEN, MCI_OPEN_ELEMENT | MCI_OPEN_TYPE, (DWORD)(LPVOID)& mciOpen);
		dwID6 = mciOpen.wDeviceID;
		mciSendCommand(dwID6, MCI_PLAY, MCI_NOTIFY, (DWORD)(LPVOID)& mciPlay);
		y = 40;
	}
}

void Mcattack(Monster* a, Charactor* b)
{
	if (b->cheat)
		;
	else
	{
		b->hp = b->hp - ((a->damage * 0.7 * puid(dre) / 100) - b->def);
		b->percent = b->hp * 100 / b->maxhp;
		PlaySound(TEXT("blood.wav"), NULL, SND_FILENAME | SND_ASYNC);
	}
	y = 10;
	if (b->hp <= 0) {
		b->hp = 0;
		b->alive = false;
		SetTimer(hWnd, 23, 1000, NULL);
		mciOpen.lpstrElementName = TEXT("Char_Death.mp3");
		mciSendCommand(0, MCI_OPEN, MCI_OPEN_ELEMENT | MCI_OPEN_TYPE, (DWORD)(LPVOID)&mciOpen);
		dwID6 = mciOpen.wDeviceID;
		mciSendCommand(dwID6, MCI_PLAY, MCI_NOTIFY, (DWORD)(LPVOID)&mciPlay);
		y = 40;
	}
}

LRESULT CALLBACK WndProc(HWND hWnd, UINT iMessage, WPARAM wParam, LPARAM lParam)
{

	PAINTSTRUCT ps; 
	HDC hdc, memdc;
	static Charactor warrior;
	static Monster mob[30];
	static POINT just, monjust,chance;
	static bool start,justout,mjustout, gameover, Victory = false, pattern = true, continuous_attack = false, left, right, up, down;
	static int count, temp, temp1, temp2, temp3;
	static int stage = 1;
	static bool played_1 = false, played_2 = false;
	int mx, my;
	static int stuntype = 0;

	static HBITMAP hBitmapMonster, hBitmapbalpan, hBitmapStage1, hBitmapHP, hBitmapSpecial, hBitmapStage2, hBitmapJust, hBitmapChance, hBitmapMenu, hBitmapKill, 
		hBitmapChance2, hBitmapEffect, hBitmapCM1, hBitmapScratch, hBitmapAD, hBitmapGameover,hBitmapStun1,hBitmapStun2,hBitmapbalpan2, hBitmapHeal,hBitmapDragon, 
		hBitmapVictory, hBitmapDanger;
	static int delay = 50, Mdelay = 1, decision, mobdelay = 50, rtcount = 0;
	switch (iMessage) {
	case WM_CREATE:
	
		mciOpen.lpstrDeviceType = TEXT("mpegvideo");
		mciOpen.lpstrElementName = TEXT("Menu.mp3");
		mciSendCommand(0, MCI_OPEN, MCI_OPEN_ELEMENT | MCI_OPEN_TYPE, (DWORD)(LPVOID)& mciOpen);
		dwID1 = mciOpen.wDeviceID;
		mciSendCommand(dwID1, MCI_PLAY, MCI_DGV_PLAY_REPEAT, (DWORD)(LPVOID)& mciPlay);
		hBitmapMonster = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP3));
		hBitmapbalpan = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP4));
		hBitmapStage1 = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP5));
		hBitmapHP = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP6));
		hBitmapSpecial = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP7));
		hBitmapStage2 = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP8));
		hBitmapJust = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP9));
		hBitmapChance = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP10));
		hBitmapMenu = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP11));
		hBitmapKill = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP12));
		hBitmapChance2 = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP13));
		hBitmapEffect = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP14));
		hBitmapCM1 = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP15));
		hBitmapScratch = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP16));
		hBitmapAD = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP17));
		hBitmapGameover = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP18));
		hBitmapStun1 = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP19));
		hBitmapStun2 = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP20));
		hBitmapbalpan2 = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP21));
		hBitmapHeal = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP22));
		hBitmapDragon = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP23));
		hBitmapVictory = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP24));
		hBitmapDanger = (HBITMAP)LoadBitmap(g_hInst, MAKEINTRESOURCE(IDB_BITMAP25));
		start = false;
		warrior.damage = 15;
		warrior.def = 5;
		warrior.hp = 100;
		warrior.mp = 10;
		warrior.maxhp = warrior.hp;
		warrior.location.x = 200;
		warrior.location.y = 375;
		warrior.percent = 100;
		warrior.special = 0;
		warrior.motion = 0;
		warrior.stage = 0;
		warrior.dodge = STOP;
		warrior.deadcount = 0;
		warrior.specialon = false;
		warrior.kill = false;
		warrior.alive = true;
		just.x = 250;
		just.y = 375;
		monjust.x = 950;
		monjust.y = 375;
		justout = false;
		chance.x = 150;
		chance.y = 375;
		for (int i = 0; i < 30; ++i)
		{
			mob[i].hp = 100 * pow(1.15, i);
			mob[i].maxhp = mob[i].hp;
			mob[i].damage = 20 * pow(1.3, i);
			mob[i].def = 5 * pow(1.15, i);
			mob[i].location.x = 1000;
			mob[i].location.y = 375;
			mob[i].percent = 100;
			mob[i].alive = false;
			mob[i].stun = false;
			if (i % 10 != 9) {
				mob[i].type = i % 10 + 1;
			}
			else if (i == 9) {
				mob[i].type = i + 1;
				mob[i].hp *= 2;
				mob[i].maxhp = mob[i].hp;
				mob[i].damage *= 1.5;
			}
			else if (i == 19) {
				mob[i].type = i + 1;
				mob[i].hp *= 3;
				mob[i].maxhp = mob[i].hp;
				mob[i].damage *= 2;
			}
		}
		mob[0].alive = true;
		break;
	case WM_LBUTTONDOWN:
		mx = LOWORD(lParam);
		my = HIWORD(lParam);
		// 시작 화면
		if (!gameover) {
			if (!start) {
				if (mx > 490 && mx < 790) {
					if (my > 440 && my < 500) {
						played_1 = true;
						mciSendCommand(dwID1, MCI_CLOSE, 0, NULL);
						mciOpen.lpstrElementName = TEXT("Battle1.mp3");
						mciSendCommand(0, MCI_OPEN, MCI_OPEN_ELEMENT | MCI_OPEN_TYPE, (DWORD)(LPVOID)& mciOpen);
						dwID3 = mciOpen.wDeviceID;
						mciSendCommand(dwID3, MCI_PLAY, MCI_DGV_PLAY_REPEAT, (DWORD)(LPVOID)& mciPlay);
						start = true;
						SetTimer(hWnd, 1, 500, NULL);
						SetTimer(hWnd, 4, 20, NULL);
						SetTimer(hWnd, 5, 5000, NULL);
						SetTimer(hWnd, 7, 3000, NULL);
					}
					else if (my > 660 && my < 720) {
						PostQuitMessage(0);
					}
				}
			}
		}
		break;

	case WM_KEYDOWN:
		if (gameover) {
			stage = 1;
			mciSendCommand(dwID2, MCI_CLOSE, 0, NULL);
			mciOpen.lpstrElementName = TEXT("Menu.mp3");
			mciSendCommand(0, MCI_OPEN, MCI_OPEN_ELEMENT | MCI_OPEN_TYPE, (DWORD)(LPVOID)& mciOpen);
			dwID1 = mciOpen.wDeviceID;
			mciSendCommand(dwID1, MCI_PLAY, MCI_DGV_PLAY_REPEAT, (DWORD)(LPVOID)& mciPlay);
			gameover = false;
			played_1 = false;
			played_2 = false;
			for (int i = 0; i < 30; ++i)
			{
				mob[i].hp = 100 * pow(1.15, i);
				mob[i].maxhp = mob[i].hp;
				mob[i].damage = 20 * pow(1.15, i);
				mob[i].def = 5 * pow(1.15, i);
				mob[i].location.x = 1000;
				mob[i].location.y = 375;
				mob[i].percent = 100;
				mob[i].alive = false;
				mob[i].stun = false;
				if (i % 10 != 9) {
					mob[i].type = i % 10 + 1;
				}
				else if (i == 9) {
					mob[i].type = i + 1;
					mob[i].hp *= 2;
					mob[i].maxhp = mob[i].hp;
					mob[i].damage *= 1.5;
				}
				else if (i == 19) {
					mob[i].type = i + 1;
					mob[i].hp *= 3;
					mob[i].maxhp = mob[i].hp;
					mob[i].damage *= 2;
				}
			}
			mob[0].alive = true;
			warrior.percent = 100;
			warrior.hp = warrior.maxhp;
			warrior.mp = 10;
			warrior.location.x = 200;
			warrior.location.y = 375;
			warrior.percent = 100;
			warrior.special = 0;
			warrior.motion = 0;
			warrior.stage = 0;
			warrior.dodge = STOP;
			warrior.specialon = false;
			warrior.kill = false;
			warrior.deadcount++;
			warrior.alive = true;
		}

		if (start && !gameover) {
			if (wParam == 'S') {
				if (warrior.mp == 10) {
					PlaySound(TEXT("Heal.wav"), NULL, SND_FILENAME | SND_ASYNC);
					warrior.hp += (warrior.maxhp / 6);
					warrior.damage *= 1.5;
					warrior.def *= 15;
					SetTimer(hWnd, 16, 3000, NULL);
					SetTimer(hWnd, 17, 500, NULL);
					warrior.mp = 0;
					warrior.percent = warrior.hp * 100 / warrior.maxhp;
					if (warrior.percent > 100) {
						warrior.percent = 100;
						warrior.hp = warrior.maxhp;
					}
				}
			}
			if (wParam == VK_F1) {
				if (!warrior.cheat)
					warrior.cheat = true;
				else
					warrior.cheat = false;
			}
			if (!warrior.behavior) {
				if (wParam == VK_SPACE) {
					PlaySound(TEXT("chain.wav"), NULL, SND_FILENAME | SND_ASYNC);
					warrior.behavior = true;
					warrior.Adirection = RIGHT;
					warrior.motion = 1;
					for (int i = 0; i < 30; ++i) {
						if (mob[i].stun) {
							if (!warrior.attack) {
								SetTimer(hWnd, 12, 10, NULL);
								warrior.attack = true;
								KillTimer(hWnd, 4);
								mob[i].location.x = 1000;
								mob[i].location.y = 375;
							}
						}
					}
					if (!warrior.attack)
						SetTimer(hWnd, 2, delay, NULL);
				}
				if (wParam == VK_UP) {
					PlaySound(TEXT("shot.wav"), NULL, SND_FILENAME | SND_ASYNC);
					warrior.behavior = true;
					warrior.MJudgement = UP;
					warrior.just = true;
					SetTimer(hWnd, 3, Mdelay, NULL);
					SetTimer(hWnd, 6, 100, NULL);
				}
				if (wParam == VK_DOWN) {
					PlaySound(TEXT("shot.wav"), NULL, SND_FILENAME | SND_ASYNC);
					warrior.behavior = true;
					warrior.MJudgement = DOWN;
					warrior.just = true;
					SetTimer(hWnd, 3, Mdelay, NULL);
					SetTimer(hWnd, 6, 100, NULL);
				}
				if (wParam == VK_LEFT) {
					PlaySound(TEXT("shot.wav"), NULL, SND_FILENAME | SND_ASYNC);
					warrior.behavior = true;
					warrior.MJudgement = LEFT;
					warrior.just = true;
					SetTimer(hWnd, 3, Mdelay, NULL);
					SetTimer(hWnd, 6, 100, NULL);
				}
				if (wParam == VK_RIGHT) {
					PlaySound(TEXT("shot.wav"), NULL, SND_FILENAME | SND_ASYNC);
					warrior.behavior = true;
					warrior.MJudgement = RIGHT;
					warrior.just = true;
					SetTimer(hWnd, 3, Mdelay, NULL);
					SetTimer(hWnd, 6, 100, NULL);
				}
				if (wParam == 'T') {
					if (warrior.special == 5) {
						mciOpen.lpstrElementName = TEXT("Skill.mp3");
						mciSendCommand(0, MCI_OPEN, MCI_OPEN_ELEMENT | MCI_OPEN_TYPE, (DWORD)(LPVOID)& mciOpen);
						dwID5 = mciOpen.wDeviceID;
						mciSendCommand(dwID5, MCI_PLAY, MCI_NOTIFY, (DWORD)(LPVOID)& mciPlay);
						warrior.behavior = true;
						warrior.Adirection = RIGHT;
						warrior.motion = 1;
						SetTimer(hWnd, 12, 10, NULL);
						SetTimer(hWnd, 14, 50, NULL);
						warrior.specialon = false;
						warrior.special = 0;
						for (int i = 0; i < 30; ++i)
						{
							if (mob[i].alive) {
								mob[i].stun = true;
								AD = true;
								SetTimer(hWnd, 11, 5000, NULL);
							}
						}
					}
				}
			}
		}
		InvalidateRect(hWnd, NULL, false);
		break;
	case WM_PAINT:
		static HDC hdc, MemDC;
		static HBITMAP BackBit, oldBackBit;
		static RECT bufferRT;
		MemDC = BeginPaint(hWnd, &ps);
		GetClientRect(hWnd, &bufferRT);
		hdc = CreateCompatibleDC(MemDC);
		BackBit = CreateCompatibleBitmap(MemDC, bufferRT.right, bufferRT.bottom);
		oldBackBit = (HBITMAP)SelectObject(hdc, BackBit);
		PatBlt(hdc, 0, 0, bufferRT.right, bufferRT.bottom, WHITENESS);
	
		if (start) {
			if (warrior.stage >= 0 && warrior.stage <= 8 || warrior.stage >= 10 && warrior.stage <= 18) {
				if (played_1 == false) {
					played_2 = false;
					mciSendCommand(dwID4, MCI_CLOSE, 0, NULL);
					mciOpen.lpstrElementName = TEXT("Battle1.mp3");
					mciSendCommand(0, MCI_OPEN, MCI_OPEN_ELEMENT | MCI_OPEN_TYPE, (DWORD)(LPVOID)& mciOpen);
					dwID3 = mciOpen.wDeviceID;
					mciSendCommand(dwID3, MCI_PLAY, MCI_DGV_PLAY_REPEAT, (DWORD)(LPVOID)& mciPlay);
					played_1 = true;
				}
			}
			if (warrior.stage == 9 || warrior.stage == 19) {
				if (played_2 == false) {
					played_1 = false;
					mciSendCommand(dwID3, MCI_CLOSE, 0, NULL);
					mciOpen.lpstrElementName = TEXT("Battle2.mp3");
					mciSendCommand(0, MCI_OPEN, MCI_OPEN_ELEMENT | MCI_OPEN_TYPE, (DWORD)(LPVOID)& mciOpen);
					dwID4 = mciOpen.wDeviceID;
					mciSendCommand(dwID4, MCI_PLAY, MCI_DGV_PLAY_REPEAT, (DWORD)(LPVOID)& mciPlay);
					played_2 = true;

				}
			}
		}
		// 시작
		if (start == false) {
			memdc = CreateCompatibleDC(hdc);
			SelectObject(memdc, hBitmapMenu);
			StretchBlt(hdc, 0, 0, 1280, 800, memdc, 0, 0, 2220, 1080, SRCCOPY);
			DeleteDC(memdc);
		}
		// 게임 오버
		if (gameover) {
			memdc = CreateCompatibleDC(hdc);
			SelectObject(memdc, hBitmapGameover);
			TransparentBlt(hdc, 0, 0, 1280, 800, memdc, 0, 0, 960, 467, RGB(255, 255, 255));
			DeleteDC(memdc);
		}
		// 승리
		if (Victory) {
			mciOpen.lpstrElementName = TEXT("victory.mp3");
			mciSendCommand(0, MCI_OPEN, MCI_OPEN_ELEMENT | MCI_OPEN_TYPE, (DWORD)(LPVOID)& mciOpen);
			dwID5 = mciOpen.wDeviceID;
			mciSendCommand(dwID5, MCI_PLAY, MCI_NOTIFY, (DWORD)(LPVOID)& mciPlay);
			memdc = CreateCompatibleDC(hdc);
			SelectObject(memdc, hBitmapVictory);
			StretchBlt(hdc, 0, 0, 1280, 800, memdc, 0, 0, 2220, 1080, SRCCOPY);
			DeleteDC(memdc);
			mciSendCommand(dwID4, MCI_CLOSE, 0, NULL);
			
		}
		if (start && !Victory) {
			// 배경 출력
			if (warrior.stage <= 9) {
				stage = 1;
				memdc = CreateCompatibleDC(hdc);
				SelectObject(memdc, hBitmapStage1);
				StretchBlt(hdc, 0, 0 - sin(x) * y, 1280, 800, memdc, 0, 0, 2200, 1080, SRCCOPY);
				DeleteDC(memdc);
			}
			else if (warrior.stage <= 20 && warrior.stage > 9) {
				memdc = CreateCompatibleDC(hdc);
				SelectObject(memdc, hBitmapStage2);
				StretchBlt(hdc, 0, 0 - sin(x) * y, 1280, 800, memdc, 0, 0, 2200, 1080, SRCCOPY);
				DeleteDC(memdc);
			}
			// 힐 아이콘
			memdc = CreateCompatibleDC(hdc);
			SelectObject(memdc, hBitmapHeal);
			TransparentBlt(hdc, 550, 600 - sin(x) * y, 100, 100, memdc, 0, 0, 169, 169, RGB(206, 206, 156));
			DeleteDC(memdc);

			// HP바, 스페셜어택바
			memdc = CreateCompatibleDC(hdc);
			SelectObject(memdc, hBitmapHP);
			TransparentBlt(hdc, 125, 600 - sin(x) * y, 200, 25, memdc, 0, 0, 311, 48, RGB(255, 255, 255));
			TransparentBlt(hdc, 134, 607 - sin(x) * y, 183, 12, memdc, 180, 24, 1, 1, RGB(255, 255, 255));
			TransparentBlt(hdc, 925, 600 - sin(x) * y, 200, 25, memdc, 0, 0, 311, 48, RGB(255, 255, 255));
			TransparentBlt(hdc, 934, 607 - sin(x) * y, 183, 12, memdc, 180, 24, 1, 1, RGB(255, 255, 255));
			TransparentBlt(hdc, 134, 607 - sin(x) * y, warrior.percent * 1.83, 12, memdc, 120, 24, 1, 1, RGB(255, 255, 255));
			TransparentBlt(hdc, 300, 150 - sin(x) * y, 600, 10, memdc, 120, 24, 1, 1, RGB(255, 255, 255));
			TransparentBlt(hdc, 300, 150 - sin(x) * y, warrior.special * 120, 10, memdc, 180, 24, 1, 1, RGB(255, 255, 255));
			TransparentBlt(hdc, 550, 600 - sin(x) * y, 100, 100 - warrior.mp * 10, memdc, 180, 24, 1, 1, RGB(255, 255, 155));
			DeleteDC(memdc);

			

			// 시스템 메시지
			if (warrior.kill) {
				memdc = CreateCompatibleDC(hdc);
				SelectObject(memdc, hBitmapKill);
				TransparentBlt(hdc, 500, 160 - sin(x) * y, 200, 70, memdc, 0, 0, 230, 92, RGB(255, 255, 255));
				DeleteDC(memdc);
			}
			if (warrior.specialon) {
				memdc = CreateCompatibleDC(hdc);
				SelectObject(memdc, hBitmapChance2);
				TransparentBlt(hdc, 350, 160 - sin(x) * y, 500, 80, memdc, 0, 0, 572, 107, RGB(255, 255, 255));
				DeleteDC(memdc);
			}
			if (AD) {
				memdc = CreateCompatibleDC(hdc);
				SelectObject(memdc, hBitmapAD);
				TransparentBlt(hdc, 350, 160 - sin(x) * y, 500, 80, memdc, 0, 0, 849, 108, RGB(255, 255, 255));
				DeleteDC(memdc);
			}
			// 발판
			if (warrior.stage <= 9) {
				memdc = CreateCompatibleDC(hdc);
				SelectObject(memdc, hBitmapbalpan);
				TransparentBlt(hdc, 150, 375 - sin(x) * y, 150, 150, memdc, 0, 0, 340, 194, RGB(255, 255, 255));
				TransparentBlt(hdc, 950, 375 - sin(x) * y, 150, 150, memdc, 0, 0, 340, 194, RGB(255, 255, 255));
				DeleteDC(memdc);
			}
			else {
				memdc = CreateCompatibleDC(hdc);
				SelectObject(memdc, hBitmapbalpan2);
				TransparentBlt(hdc, 150, 390 - sin(x) * y, 150, 125, memdc, 0, 0, 324, 137, RGB(255, 255, 255));
				TransparentBlt(hdc, 950, 390 - sin(x) * y, 150, 125, memdc, 0, 0, 324, 137, RGB(255, 255, 255));
				DeleteDC(memdc);
			}

			// 몬스터 출력
			for (int i = 0; i < 30; ++i)
			{
				if (mob[i].alive)
				{
					memdc = CreateCompatibleDC(hdc);
					SelectObject(memdc, hBitmapMonster);
					if (mob[i].type == 1) {					// 식인꽃
						TransparentBlt(hdc, mob[i].location.x - 50 - sin(x) * y, mob[i].location.y - 50 - sin(x) * y, 150, 150, memdc, 520, 300, 280, 300, RGB(255, 255, 255));
					}
					if (mob[i].type == 2) {					// 돌거북
						TransparentBlt(hdc, mob[i].location.x - 70 - sin(x) * y, mob[i].location.y - 35 - sin(x) * y, 150, 150, memdc, 1250, 0, 330, 200, RGB(255, 255, 255));
					}
					if (mob[i].type == 3) {					// 스콜피온
						TransparentBlt(hdc, mob[i].location.x - 75 - sin(x) * y, mob[i].location.y - 75 - sin(x) * y, 200, 200, memdc, 250, 300, 260, 300, RGB(255, 255, 255));
					}
					if (mob[i].type == 4) {					// 설인
						TransparentBlt(hdc, mob[i].location.x - 140- sin(x) * y, mob[i].location.y - 150 - sin(x) * y, 300, 300, memdc, 0, 300, 260, 300, RGB(255, 255, 255));
					}
					if (mob[i].type == 5) {					// 골렘
						TransparentBlt(hdc, mob[i].location.x - 140 - sin(x) * y, mob[i].location.y - 180 - sin(x) * y, 300, 300, memdc, 250, 0, 260, 300, RGB(255, 255, 255));
					}
					if (mob[i].type == 6) {					// 늑대
						TransparentBlt(hdc, mob[i].location.x - 100 - sin(x) * y, mob[i].location.y - 65 - sin(x) * y, 200, 150, memdc, 1250, 175, 310, 220, RGB(255, 255, 255));
					}
					if (mob[i].type == 7) {					// 노루
						TransparentBlt(hdc, mob[i].location.x - 70 - sin(x) * y, mob[i].location.y - 150 - sin(x) * y, 200, 250, memdc, 750, 0, 250, 300, RGB(255, 255, 255));
					}
					if (mob[i].type == 8) {					// 스켈레톤
						TransparentBlt(hdc, mob[i].location.x - 85 - sin(x) * y, mob[i].location.y - 200 - sin(x) * y, 200, 300, memdc, 1000, 0, 260, 300, RGB(255, 255, 255));
					}
					if (mob[i].type == 9) {					// 주시자
						TransparentBlt(hdc, mob[i].location.x - 85 - sin(x) * y, mob[i].location.y - 200 - sin(x) * y, 200, 300, memdc, 765, 300, 250, 300, RGB(255, 255, 255));
					}
					if (mob[i].type == 10) {				// 보스몹 거인
						TransparentBlt(hdc, mob[i].location.x - 140 - sin(x) * y, mob[i].location.y - 180 - sin(x) * y, 280, 300, memdc, 0, 0, 280, 300, RGB(255, 255, 255));
					}
					DeleteDC(memdc);
					if (mob[i].type == 20) {				// 용
						memdc = CreateCompatibleDC(hdc);
						SelectObject(memdc, hBitmapDragon);
						TransparentBlt(hdc, mob[i].location.x - 140 - sin(x) * y, mob[i].location.y - 180 - sin(x) * y, 419, 295, memdc, 0, 0, 419, 295, RGB(206, 206, 156));
						DeleteDC(memdc);
					}
					if (mob[i].stun) {
						memdc = CreateCompatibleDC(hdc);
						SelectObject(memdc, hBitmapStun1);
						if (mob[i].type == 1) {					// 식인꽃
							TransparentBlt(hdc, mob[i].location.x - 110 - sin(x) * y, mob[i].location.y - 150 - sin(x) * y, 255, 99, memdc, 0, 0, 245, 111, RGB(206, 206, 156));
						}
						if (mob[i].type == 2) {					// 돌거북
							TransparentBlt(hdc, mob[i].location.x - 110 - sin(x) * y, mob[i].location.y - 135 - sin(x) * y, 255, 99, memdc, 0, 0, 245, 111, RGB(206, 206, 156));
						}
						if (mob[i].type == 3) {					// 스콜피온
							TransparentBlt(hdc, mob[i].location.x - 110 - sin(x) * y, mob[i].location.y - 175 - sin(x) * y, 255, 99, memdc, 0, 0, 245, 111, RGB(206, 206, 156));
						}
						if (mob[i].type == 4) {					// 설인
							TransparentBlt(hdc, mob[i].location.x - 110 - sin(x) * y, mob[i].location.y - 250 - sin(x) * y, 255, 99, memdc, 0, 0, 245, 111, RGB(206, 206, 156));
						}
						if (mob[i].type == 5) {					// 골렘
							TransparentBlt(hdc, mob[i].location.x - 110 - sin(x) * y, mob[i].location.y - 280 - sin(x) * y, 255, 99, memdc, 0, 0, 245, 111, RGB(206, 206, 156));
						}
						if (mob[i].type == 6) {					// 늑대
							TransparentBlt(hdc, mob[i].location.x - 110 - sin(x) * y, mob[i].location.y - 165 - sin(x) * y, 255, 99, memdc, 0, 0, 245, 111, RGB(206, 206, 156));
						}
						if (mob[i].type == 7) {					// 노루
							TransparentBlt(hdc, mob[i].location.x - 110 - sin(x) * y, mob[i].location.y - 250 - sin(x) * y, 255, 99, memdc, 0, 0, 245, 111, RGB(206, 206, 156));
						}
						if (mob[i].type == 8) {					// 스켈레톤
							TransparentBlt(hdc, mob[i].location.x - 110 - sin(x) * y, mob[i].location.y - 300 - sin(x) * y, 255, 99, memdc, 0, 0, 245, 111, RGB(206, 206, 156));
						}
						if (mob[i].type == 9) {					// 주시자
							TransparentBlt(hdc, mob[i].location.x - 110 - sin(x) * y, mob[i].location.y - 300 - sin(x) * y, 255, 99, memdc, 0, 0, 245, 111, RGB(206, 206, 156));
						}
						if (mob[i].type == 10) {				// 보스몹 거인
							TransparentBlt(hdc, mob[i].location.x - 110 - sin(x) * y, mob[i].location.y - 250 - sin(x) * y, 255, 99, memdc, 0, 0, 245, 111, RGB(206, 206, 156));
						}
						if (mob[i].type == 19) {				// 용
							TransparentBlt(hdc, mob[i].location.x - 110 - sin(x) * y, mob[i].location.y - 250 - sin(x) * y, 255, 99, memdc, 0, 0, 245, 111, RGB(206, 206, 156));
						}
						DeleteDC(memdc);
					}
					memdc = CreateCompatibleDC(hdc);
					SelectObject(memdc, hBitmapHP);
					TransparentBlt(hdc, 934, 607 - sin(x) * y, mob[i].percent * 1.83, 12, memdc, 120, 24, 1, 1, RGB(255, 255, 255));
					DeleteDC(memdc);
				}
			}
			if (warrior.specialon) {
				memdc = CreateCompatibleDC(hdc);
				SelectObject(memdc, hBitmapEffect);
				TransparentBlt(hdc, warrior.location.x - 165, warrior.location.y - 135 - sin(x) * y, 400, 400, memdc, 0, 0, 540, 520, RGB(206, 206, 156));
				DeleteDC(memdc);
			}
			// 캐릭터 출력
			if (warrior.alive) {
				if (!warrior.motion) {
					memdc = CreateCompatibleDC(hdc);
					SelectObject(memdc, hBitmapMonster);
					TransparentBlt(hdc, warrior.location.x - 25, warrior.location.y - 15 - sin(x) * y, 125, 125, memdc, 1000, 300, 200, 200, RGB(255, 255, 255));
					DeleteDC(memdc);
				}
				else if (warrior.motion == 1) {
					memdc = CreateCompatibleDC(hdc);
					SelectObject(memdc, hBitmapCM1);
					TransparentBlt(hdc, warrior.location.x - 25, warrior.location.y - 15 - sin(x) * y, 100, 111, memdc, 0, 0, 87, 98, RGB(206, 206, 156));
					DeleteDC(memdc);
				}
				else if (warrior.motion == 2) {
					memdc = CreateCompatibleDC(hdc);
					SelectObject(memdc, hBitmapMonster);
					TransparentBlt(hdc, warrior.location.x - 20, warrior.location.y - 20 - sin(x) * y - 20, 175, 175, memdc, 1000, 500, 250, 300, RGB(255, 255, 255));
					DeleteDC(memdc);
				}
			}
			// 연속 공격 범위 표시
			if (warrior.alive) {
				if (right) {
					memdc = CreateCompatibleDC(hdc);
					SelectObject(memdc, hBitmapDanger);
					TransparentBlt(hdc, 120 - sin(x) * y, 300 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					TransparentBlt(hdc, 120 - sin(x) * y, 350 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					TransparentBlt(hdc, 120 - sin(x) * y, 400 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					TransparentBlt(hdc, 120 - sin(x) * y, 450 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					DeleteDC(memdc);
				}
				if (left) {
					memdc = CreateCompatibleDC(hdc);
					SelectObject(memdc, hBitmapDanger);
					TransparentBlt(hdc, 240 - sin(x) * y, 300 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					TransparentBlt(hdc, 240 - sin(x) * y, 350 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					TransparentBlt(hdc, 240 - sin(x) * y, 400 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					TransparentBlt(hdc, 240 - sin(x) * y, 450 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					DeleteDC(memdc);
				}
				if (up) {
					memdc = CreateCompatibleDC(hdc);
					SelectObject(memdc, hBitmapDanger);
					TransparentBlt(hdc, 100 - sin(x) * y, 450 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					TransparentBlt(hdc, 150 - sin(x) * y, 450 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					TransparentBlt(hdc, 200 - sin(x) * y, 450 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					TransparentBlt(hdc, 250 - sin(x) * y, 450 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					DeleteDC(memdc);
				}
				if (down) {
					memdc = CreateCompatibleDC(hdc);
					SelectObject(memdc, hBitmapDanger);
					TransparentBlt(hdc, 100 - sin(x) * y, 300 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					TransparentBlt(hdc, 150 - sin(x) * y, 300 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					TransparentBlt(hdc, 200 - sin(x) * y, 300 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					TransparentBlt(hdc, 250 - sin(x) * y, 300 - sin(x) * y, 100, 100, memdc, 0, 0, 305, 297, RGB(255, 255, 255));
					DeleteDC(memdc);
				}
			}


			// just 출력
			if (justout) {
				memdc = CreateCompatibleDC(hdc);
				SelectObject(memdc, hBitmapJust);
				TransparentBlt(hdc, just.x, just.y, 125, 30, memdc, 0, 0, 297, 96, RGB(255, 255, 255));
				DeleteDC(memdc);
			}
			if (mjustout) {
				memdc = CreateCompatibleDC(hdc);
				SelectObject(memdc, hBitmapJust);
				TransparentBlt(hdc, monjust.x, monjust.y, 125, 30, memdc, 0, 0, 297, 96, RGB(255, 255, 255));
				DeleteDC(memdc);
			}
			// chance 출력
			if (warrior.specialon) {
				memdc = CreateCompatibleDC(hdc);
				SelectObject(memdc, hBitmapChance);
				TransparentBlt(hdc, chance.x, chance.y, 125, 30, memdc, 0, 0, 419, 93, RGB(255, 255, 255));
				DeleteDC(memdc);
			}
		}

		GetClientRect(hWnd, &bufferRT);
		BitBlt(MemDC, 0, 0, bufferRT.right, bufferRT.bottom, hdc, 0, 0, SRCCOPY);
		SelectObject(hdc, oldBackBit);
		DeleteObject(BackBit);
		DeleteDC(hdc);
		EndPaint(hWnd, &ps);
		break;
	case WM_TIMER:
		switch (wParam) {
		// 몬스터 생성 타이머
		case 1:
			if (warrior.stage == 20) {
				Victory = true;
				SetTimer(hWnd, 15, 4800, NULL);
			}
			mob[warrior.stage].alive = true;
			// 몬스터 공격 주기 설정
			SetTimer(hWnd, 5, 5000, NULL);
			warrior.kill = false;
			mjust = true;
			SetTimer(hWnd, 6, 500, NULL);
			KillTimer(hWnd, 1);
			break;
		// 캐릭터 공격 타이머
		case 2:
				SetTimer(hWnd, 2, delay, NULL);
				if (warrior.location.y == 375) {
					if (warrior.location.x >= 200 && warrior.location.x < 900 && warrior.Adirection == RIGHT) {
						warrior.location.x += 70;
						delay -= 5;
					}
					else if (warrior.location.x == 900 && warrior.Adirection == RIGHT) {
						for (int i = 0; i < 30; ++i) {
							if (mob[i].alive && !mob[i].attack) {
								Cattack(&warrior, &mob[i]);
								SetTimer(hWnd, 14, 50, NULL);
								if (mjust == true) {
									mjustout = true;
									SetTimer(hWnd, 8, 50, NULL);
								}
								if (!mob[i].alive) {
									SetTimer(hWnd, 1, 3000, NULL);				// 죽었을 때 몬스터 생성 타이머 다시 돌림
								}
							}
						}
						warrior.motion = 2;
						delay = 500;
						warrior.Adirection = LEFT;
					}
					else if (warrior.location.x > 200 && warrior.location.x <= 900 && warrior.Adirection == LEFT) {
						if (delay == 500) {
							delay = 50;
						}
						if (warrior.location.x == 760)
							warrior.motion = 1;
						warrior.location.x -= 70;
						delay -= 5;
					}
					else if (warrior.location.x == 200 && warrior.Adirection == LEFT)
						warrior.Adirection = STOP;
					else if (warrior.Adirection == STOP) {
						warrior.behavior = false;
						delay = 50;
						KillTimer(hWnd, 2);
						warrior.motion = 0;
					}
				}

			break;
		// 캐릭터 회피 타이머
		case 3:
				switch (warrior.MJudgement) {
				case UP:
					if (warrior.location.x == 200 && warrior.location.y == 375) {
						warrior.location.y -= 150;
						warrior.MJudgement = DOWN;
						Mdelay = 1000;
						warrior.dodge = UP;
						SetTimer(hWnd, 3, Mdelay, NULL);
					}
					else {
						warrior.location.y -= 150;
						warrior.MJudgement = STOP;
						Mdelay = 1;
						warrior.dodge = STOP;
						SetTimer(hWnd, 3, Mdelay, NULL);
					}
					break;
				case DOWN:
					if (warrior.location.x == 200 && warrior.location.y == 375) {
						warrior.location.y += 150;
						warrior.MJudgement = UP;
						Mdelay = 1000;
						warrior.dodge = DOWN;
						SetTimer(hWnd, 3, Mdelay, NULL);

					}
					else {
						warrior.location.y += 150;
						warrior.MJudgement = STOP; 
						warrior.dodge = STOP;
						Mdelay = 1;
						SetTimer(hWnd, 3, Mdelay, NULL);
					}
					break;
				case LEFT:
					if (warrior.location.x == 200 && warrior.location.y == 375) {
						warrior.location.x -= 150;
						warrior.MJudgement = RIGHT;
						Mdelay = 1000;
						warrior.dodge = LEFT;
						SetTimer(hWnd, 3, Mdelay, NULL);
					}
					else {
						warrior.location.x -= 150;
						warrior.MJudgement = STOP;
						Mdelay = 1;
						warrior.dodge = STOP;
						SetTimer(hWnd, 3, Mdelay, NULL);
					}
					break;
				case RIGHT:
					if (warrior.location.x == 200 && warrior.location.y == 375) {
						warrior.location.x += 150;
						warrior.MJudgement = LEFT;
						Mdelay = 1000;
						warrior.dodge = RIGHT;
						SetTimer(hWnd, 3, Mdelay, NULL);
					}
					else {
						warrior.location.x += 150;
						warrior.MJudgement = STOP;
						Mdelay = 1;
						warrior.dodge = STOP;
						SetTimer(hWnd, 3, Mdelay, NULL);
					}
					break;
				case STOP:
					warrior.behavior = false;
					KillTimer(hWnd, 3);
				}
			break;
		case 4:
		// 몬스터 공격 타이머
			SetTimer(hWnd, 4, mobdelay, NULL);
			for (int i = 0; i < 30; ++i)
			{
				if (mob[i].alive)
				{
				switch (mob[i].pattern) {
					case 1:
						if (mob[i].location.x >= 1000 && mob[i].location.x < 1100 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 250, NULL);
							mob[i].location.x += 50;
						}
						else if (mob[i].location.x == 1100 && mob[i].Adirection == RIGHT) {
							mob[i].Adirection = LEFT;
							SetTimer(hWnd, 4, 500, NULL);
							mob[i].attack = true;
						}
						else if (mob[i].location.x <= 1100 && mob[i].location.x > 200 && mob[i].Adirection == LEFT) {
							if (mobdelay == 500) {
								mobdelay = 50;
							}
							mob[i].location.x -= 90;
							if (mobdelay != 5) {
								mobdelay -= 5;
							}
						}
						else if (mob[i].location.x == 200 && mob[i].Adirection == LEFT) {
							if (warrior.dodge != UP && warrior.dodge != DOWN) {
								Mattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else if (warrior.just) {
								if (warrior.special < 4)
									warrior.special += 2;
								else if (warrior.special == 4)
									warrior.special += 1;
								Mdelay = 1;
								SetTimer(hWnd, 3, Mdelay, NULL);
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
							}
							else if (warrior.special < 5) {
								warrior.special++;
							}
							if (warrior.special == 5) {
								SetTimer(hWnd, 9, 2000, NULL);
								warrior.specialon = true;
								SetTimer(hWnd, 10, 50, NULL);
							}
							mob[i].Adirection = RIGHT;
							mobdelay = 100;
							mob[i].attack = false;
						}
						else if (mob[i].location.x >= 200 && mob[i].location.x < 1000 && mob[i].Adirection == RIGHT) {
							if (mobdelay == 100) {
								mobdelay = 50;
							}
							mob[i].location.x += 80;
							mobdelay -= 5;
						}
						if (mob[i].location.x == 1000 && mob[i].Adirection == RIGHT)
							mob[i].Adirection = STOP;
						if (mob[i].Adirection == STOP) {
							mobdelay = 50;
							KillTimer(hWnd, 4);
						}
						break;
					case 2:
						if (mob[i].location.x >= 1000 && mob[i].location.x < 1100 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 250, NULL);
							mob[i].location.x += 50;
						}
						else if (mob[i].location.x == 1100 && mob[i].Adirection != LEFT) {
							 if (mob[i].location.y == 375 && rtcount == 4) {
								rtcount = 0;
								mob[i].Adirection = LEFT;
								SetTimer(hWnd, 4, 500, NULL);
								mob[i].attack = true;
							}
							else if (mob[i].location.y > 305 && mob[i].Adirection != DOWN) {
								mobdelay = 20;
								mob[i].location.y -= 35;
							}
							else if (mob[i].location.y == 305) {
								mob[i].location.y += 35;
								mob[i].Adirection = DOWN;
								rtcount++;
							}
							else if (mob[i].location.y < 445 && mob[i].Adirection == DOWN) {
								mob[i].location.y += 35;
							}
							else if (mob[i].location.y == 445) {
								mob[i].location.y += 35;
								mob[i].Adirection = UP;
								rtcount++;
							}
						}
						else if (mob[i].location.x <= 1100 && mob[i].location.x > 300 && mob[i].Adirection == LEFT) {
							if (mobdelay == 500 || mobdelay == 50) {
								mobdelay = 50;
							}
							if (mobdelay != 5) {
								mobdelay -= 5;
							}
							mob[i].location.x -= 80;
						}
						else if (mob[i].location.x == 300 && mob[i].Adirection == LEFT) {
							if (warrior.dodge != LEFT) {
								Mattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else if (warrior.just) {
								if (warrior.special < 4)
									warrior.special += 2;
								else if (warrior.special == 4)
									warrior.special += 1;
									
								Mdelay = 1;
								SetTimer(hWnd, 3, Mdelay, NULL);
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
							}
							else if (warrior.special < 5) {
								warrior.special++;
							}
							if (warrior.special == 5) {
								SetTimer(hWnd, 9, 2000, NULL);
								warrior.specialon = true;
								SetTimer(hWnd, 10, 50, NULL);
							}
							mob[i].Adirection = RIGHT;
							mobdelay = 100;
							mob[i].attack = false;
						}
						else if (mob[i].location.x >= 300 && mob[i].location.x < 1000 && mob[i].Adirection == RIGHT) {
							if (mobdelay == 100) {
								mobdelay = 50;
							}
							mob[i].location.x += 70;
							mobdelay -= 5;
						}
						if (mob[i].location.x == 1000 && mob[i].Adirection == RIGHT)
							mob[i].Adirection = STOP;
						if (mob[i].Adirection == STOP) {
							mobdelay = 50;
							KillTimer(hWnd, 4);
						}
						break;
					case 3:
						if (mob[i].location.x >= 1000 && mob[i].location.x < 1100 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 25, NULL);
							mob[i].location.x += 5;
							mob[i].location.y = -sin(mob[i].location.x * PI / 100) * 50 + 375;
						}
						else if (mob[i].location.x == 1100 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 500, NULL);
							mob[i].Adirection = LEFT;
							mob[i].attack = true;
						}
						else if (mob[i].location.x > 200 && mob[i].Adirection == LEFT) {
							if (mobdelay == 500) {
								mobdelay = 50;
							}
							if (mobdelay != 5) {
								mobdelay -= 5;
							}
							mob[i].location.x -= 90;
							mob[i].location.y = -sin((mob[i].location.x - 200) * PI / 900) * 200 + 375;
						}
						else if (mob[i].location.x == 200 && mob[i].Adirection == LEFT){
							if (warrior.dodge != DOWN) {
								Mattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else if (warrior.just) {
								if (warrior.special < 4)
									warrior.special += 2;
								else if (warrior.special == 4)
									warrior.special += 1;

								Mdelay = 1;
								SetTimer(hWnd, 3, Mdelay, NULL);
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
							}
							else if (warrior.special < 5) {
								warrior.special++;
							}
							if (warrior.special == 5) {
								SetTimer(hWnd, 9, 2000, NULL);
								warrior.specialon = true;
								SetTimer(hWnd, 10, 50, NULL);
							}
							mob[i].Adirection = RIGHT;
							mobdelay = 100;
							mob[i].attack = false;
						}
						else if (mob[i].location.x >= 200 && mob[i].location.x < 1000 && mob[i].Adirection == RIGHT) {
							if (mobdelay == 100) {
								mobdelay = 50;
							}
							mob[i].location.x += 80;
							mobdelay -= 5;
						}
						if (mob[i].location.x == 1000 && mob[i].Adirection == RIGHT)
							mob[i].Adirection = STOP;
						if (mob[i].Adirection == STOP) {
							mobdelay = 50;
							KillTimer(hWnd, 4);
						}
						break;
					case 4:
						if (mob[i].location.x >= 1000 && mob[i].location.x < 1100 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 25, NULL);
							mob[i].location.x += 5;
							mob[i].location.y = sin(mob[i].location.x * PI / 100) * 50 + 375;
						}
						else if (mob[i].location.x == 1100 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 500, NULL);
							mob[i].Adirection = LEFT;
							mob[i].attack = true;
						}
						else if (mob[i].location.x > 200 && mob[i].Adirection == LEFT) {
							if (mobdelay == 500) {
								mobdelay = 50;
							}
							if (mobdelay != 5) {
								mobdelay -= 5;
							}
							mob[i].location.x -= 90;
							mob[i].location.y = sin((mob[i].location.x - 200) * PI / 900) * 200 + 375;
						}
						else if (mob[i].location.x == 200 && mob[i].Adirection == LEFT) {
							if (warrior.dodge != UP) {
								Mattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else if (warrior.just) {
								if (warrior.special < 4)
									warrior.special += 2;
								else if (warrior.special == 4)
									warrior.special += 1;

								Mdelay = 1;
								SetTimer(hWnd, 3, Mdelay, NULL);
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
							}
							else if (warrior.special < 5) {
								warrior.special++;
							}
							if (warrior.special == 5) {
								SetTimer(hWnd, 9, 2000, NULL);
								warrior.specialon = true;
								SetTimer(hWnd, 10, 50, NULL);
							}
							mob[i].Adirection = RIGHT;
							mobdelay = 100;
							mob[i].attack = false;
						}
						else if (mob[i].location.x >= 200 && mob[i].location.x < 1000 && mob[i].Adirection == RIGHT) {
							if (mobdelay == 100) {
								mobdelay = 50;
							}
							mob[i].location.x += 80;
							mobdelay -= 5;
						}
						if (mob[i].location.x == 1000 && mob[i].Adirection == RIGHT)
							mob[i].Adirection = STOP;
						if (mob[i].Adirection == STOP) {
							mobdelay = 50;
							KillTimer(hWnd, 4);
						}
						break;
					case 5:
						if (mob[i].location.x >= 1000 && mob[i].location.x < 1100 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 25, NULL);
							mob[i].location.x += 5;
							mob[i].location.y += 5;
						}
						else if (mob[i].location.x == 1100 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 500, NULL);
							mob[i].Adirection = LEFT;
							mob[i].attack = true;
						}
						else if (mob[i].location.x > 200 && mob[i].Adirection == LEFT) {
							if (mobdelay == 500) {
								mobdelay = 50;
							}
							if (mobdelay != 5) {
								mobdelay -= 5;
							}
							mob[i].location.x -= 90;
							mob[i].location.y = (mob[i].location.x - 300) / 8 + 375;
						}
						else if (mob[i].location.x == 200 && mob[i].Adirection == LEFT) {
							if (warrior.dodge != DOWN) {
								Mattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else if (warrior.just) {
								if (warrior.special < 4)
									warrior.special += 2;
								else if (warrior.special == 4)
									warrior.special += 1;

								Mdelay = 1;
								SetTimer(hWnd, 3, Mdelay, NULL);
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
							}
							else if (warrior.special < 5) {
								warrior.special++;
							}
							if (warrior.special == 5) {
								SetTimer(hWnd, 9, 2000, NULL);
								warrior.specialon = true;
								SetTimer(hWnd, 10, 50, NULL);
							}
							mob[i].Adirection = RIGHT;
							mobdelay = 100;
							mob[i].attack = false;
						}
						else if (mob[i].location.x >= 200 && mob[i].location.x < 1000 && mob[i].Adirection == RIGHT) {
							if (mobdelay == 100) {
								mobdelay = 50;
							}
							mob[i].location.x += 80;
							mobdelay -= 5;
						}
						if (mob[i].location.x == 1000 && mob[i].Adirection == RIGHT)
							mob[i].Adirection = STOP;
						if (mob[i].Adirection == STOP) {
							mobdelay = 50;
							KillTimer(hWnd, 4);
						}
						break;
					case 6:
						if (mob[i].location.x >= 1000 && mob[i].location.x < 1100 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 25, NULL);
							mob[i].location.x += 5;
							mob[i].location.y -= 5;
						}
						else if (mob[i].location.x == 1100 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 500, NULL);
							mob[i].Adirection = LEFT;
							mob[i].attack = true;
						}
						else if (mob[i].location.x > 200 && mob[i].Adirection == LEFT) {
							if (mobdelay == 500) {
								mobdelay = 50;
							}
							if (mobdelay != 5) {
								mobdelay -= 5;
							}
							mob[i].location.x -= 90;
							mob[i].location.y = -((mob[i].location.x - 300) / 8) + 475;
						}
						else if (mob[i].location.x == 200 && mob[i].Adirection == LEFT) {
							if (warrior.dodge != UP) {
								Mattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else if (warrior.just) {
								if (warrior.special < 4)
									warrior.special += 2;
								else if (warrior.special == 4)
									warrior.special += 1;

								Mdelay = 1;
								SetTimer(hWnd, 3, Mdelay, NULL);
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
							}
							else if (warrior.special < 5) {
								warrior.special++;
							}
							if (warrior.special == 5) {
								SetTimer(hWnd, 9, 2000, NULL);
								warrior.specialon = true;
								SetTimer(hWnd, 10, 50, NULL);
							}
							mob[i].Adirection = RIGHT;
							mobdelay = 100;
							mob[i].attack = false;
						}
						else if (mob[i].location.x >= 200 && mob[i].location.x < 1000 && mob[i].Adirection == RIGHT) {
							if (mobdelay == 100) {
								mobdelay = 50;
							}
							mob[i].location.x += 80;
							mobdelay -= 5;
						}
						if (mob[i].location.x == 1000 && mob[i].Adirection == RIGHT)
							mob[i].Adirection = STOP;
						if (mob[i].Adirection == STOP) {
							mobdelay = 50;
							mob[i].location.y -= 100;
							KillTimer(hWnd, 4);
						}
						break;
					case 7:
						if (mob[i].location.x == 1000 && mob[i].location.y > 275 && mob[i].location.y <= 375 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 25, NULL);
							mob[i].location.y -= 5;
						}
						else if (mob[i].location.x >= 1000 && mob[i].location.x < 1100 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 25, NULL);
							mob[i].location.x += 5;
						}
						else if (mob[i].location.x == 1100 && mob[i].Adirection == RIGHT) {
							mob[i].Adirection = LEFT;
							SetTimer(hWnd, 4, 500, NULL);
							mob[i].attack = true;
						}
						else if (mob[i].location.x <= 1100 && mob[i].location.x > 200 && mob[i].Adirection == LEFT) {
							if (mobdelay == 500) {
								mobdelay = 50;
							}
							mob[i].location.x -= 90;
							if (mobdelay != 5) {
								mobdelay -= 5;
							}
						}
						else if (mob[i].location.x == 200 && mob[i].Adirection == LEFT) {
							if (warrior.dodge != DOWN) {
								Mattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else if (warrior.just) {
								if (warrior.special < 4)
									warrior.special += 2;
								else if (warrior.special == 4)
									warrior.special += 1;
								Mdelay = 1;
								SetTimer(hWnd, 3, Mdelay, NULL);
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
							}
							else if (warrior.special < 5) {
								warrior.special++;
							}
							if (warrior.special == 5) {
								SetTimer(hWnd, 9, 2000, NULL);
								warrior.specialon = true;
								SetTimer(hWnd, 10, 50, NULL);
							}
							mob[i].Adirection = RIGHT;
							mobdelay = 100;
							mob[i].attack = false;
						}
						else if (mob[i].location.x >= 200 && mob[i].location.x < 1000 && mob[i].Adirection == RIGHT) {
							if (mobdelay == 100) {
								mobdelay = 50;
							}
							mob[i].location.x += 80;
							mobdelay -= 5;
							if (mob[i].location.x == 1000 && mob[i].Adirection == RIGHT) {
								mob[i].location.y = 375;
								mobdelay = 50;
								KillTimer(hWnd, 4);
							}
						}
						break;
					case 8:
						if (mob[i].location.x == 1000 && mob[i].location.y >= 375 && mob[i].location.y < 475 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 25, NULL);
							mob[i].location.y += 5;
						}
						else if (mob[i].location.x >= 1000 && mob[i].location.x < 1100 && mob[i].Adirection == RIGHT) {
							SetTimer(hWnd, 4, 25, NULL);
							mob[i].location.x += 5;
						}
						else if (mob[i].location.x == 1100 && mob[i].Adirection == RIGHT) {
							mob[i].Adirection = LEFT;
							SetTimer(hWnd, 4, 500, NULL);
							mob[i].attack = true;
						}
						else if (mob[i].location.x <= 1100 && mob[i].location.x > 200 && mob[i].Adirection == LEFT) {
							if (mobdelay == 500) {
								mobdelay = 50;
							}
							mob[i].location.x -= 90;
							if (mobdelay != 5) {
								mobdelay -= 5;
							}
						}
						else if (mob[i].location.x == 200 && mob[i].Adirection == LEFT) {
							if (warrior.dodge != UP) {
								Mattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else if (warrior.just) {
								if (warrior.special < 4)
									warrior.special += 2;
								else if (warrior.special == 4)
									warrior.special += 1;
								Mdelay = 1;
								SetTimer(hWnd, 3, Mdelay, NULL);
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
							}
							else if (warrior.special < 5) {
								warrior.special++;
							}
							if (warrior.special == 5) {
								SetTimer(hWnd, 9, 2000, NULL);
								warrior.specialon = true;
								SetTimer(hWnd, 10, 50, NULL);
							}
							mob[i].Adirection = RIGHT;
							mobdelay = 100;
							mob[i].attack = false;
						}
						else if (mob[i].location.x >= 200 && mob[i].location.x < 1000 && mob[i].Adirection == RIGHT) {
							if (mobdelay == 100) {
								mobdelay = 50;
							}
							mob[i].location.x += 80;
							mobdelay -= 5;
							if (mob[i].location.x == 1000 && mob[i].Adirection == RIGHT) {
								mob[i].location.y = 375;
								mobdelay = 50;
								KillTimer(hWnd, 4);
							}
						}
						break;
					case 9:
						if (pattern) {
							SetTimer(hWnd, 4, 250, NULL);
							if (i == 19)						// 공격 횟수 설정
								SetTimer(hWnd, 18, 1, NULL);
							SetTimer(hWnd, 19, 501, NULL);
							SetTimer(hWnd, 20, 1001, NULL);
							SetTimer(hWnd, 21, 1501, NULL);
							KillTimer(hWnd, 5);
							motion = true;
							pattern = false;
							mob[i].attack = true;
						}
						if (motion) {
							if (rtcount == 8) {
								rtcount = 0;
								motion = false;
								mob[i].location.x = 1000;
							}
							else if (mob[i].location.x >= 900 && mob[i].location.x < 1100 && mob[i].Adirection == RIGHT) {
								mobdelay = 20;
								mob[i].location.x += 25;
							}
							else if (mob[i].location.x == 900 && mob[i].Adirection == LEFT) {
								mob[i].location.x += 25;
								mob[i].Adirection = RIGHT;
								rtcount++;
							}
							else if (mob[i].location.x > 900 && mob[i].location.x <= 1100 && mob[i].Adirection == LEFT) {
								mob[i].location.x -= 25;
							}
							else if (mob[i].location.x == 1100 && mob[i].Adirection == RIGHT) {
								mob[i].location.x -= 25;
								mob[i].Adirection = LEFT;
								rtcount++;
							}
						}
						else {
							pattern = true;
							KillTimer(hWnd, 4);
						}
						break;
					}
				}
			}
			if (!warrior.alive) {
				
				KillTimer(hWnd, 5);
				KillTimer(hWnd, 1);
				KillTimer(hWnd, 7);
				SetTimer(hWnd, 13, 2000, NULL);
				KillTimer(hWnd, 4);
			}
			break; 
		// 몬스터 패턴 설정 타이머
		case 5:
			SetTimer(hWnd, 5, 5000, NULL);
			for (int i = 0; i < 30; ++i)
			{
				if (mob[i].alive)
				{
					mob[i].Adirection = RIGHT;
					decision = uid(dre);
					switch (mob[i].type)
					{
					case 1:
						mob[i].pattern = 1;
						SetTimer(hWnd, 4, 500, NULL);
						break;
					case 2:
						while (1) {
							decision = uid(dre);
							if (decision < 2)
								break;
						}
						if (decision == 0)
							mob[i].pattern = 1;
						else if (decision == 1)
							mob[i].pattern = 2;
						SetTimer(hWnd, 4, 500, NULL);
						break;
					case 3:
						while (1) {
							decision = uid(dre);
							if (decision != 3)
								break;
						}
 						if (decision == 0)
							mob[i].pattern = 1;
						else if (decision == 1)
							mob[i].pattern = 7;
						else
							mob[i].pattern = 8;
						SetTimer(hWnd, 4, 500, NULL);
						break;
					case 4:
						while (1) {
							decision = uid(dre);
							if (decision != 3)
								break;
						}
						if (decision == 0)
							mob[i].pattern = 1;
						else if (decision == 1)
							mob[i].pattern = 3;
						else if (decision == 2) 
							mob[i].pattern = 4;
						SetTimer(hWnd, 4, 500, NULL);
						break;
					case 5:
						if (decision == 0)
							mob[i].pattern = 3;
						else if (decision == 1)
							mob[i].pattern = 4;
						else if (decision == 2)
							mob[i].pattern = 5;
						else
							mob[i].pattern = 6;
						SetTimer(hWnd, 4, 500, NULL);
						break;
					case 6:
						while (1) {
							decision = uid(dre);
							if (decision != 3)
								break;
						}
						if (decision == 0)
							mob[i].pattern = 1;
						else if (decision == 1)
							mob[i].pattern = 5;
						else
							mob[i].pattern = 6;
						SetTimer(hWnd, 4, 500, NULL);
						break;
					case 7:
						if (decision == 0)
							mob[i].pattern = 1;
						else if (decision == 1)
							mob[i].pattern = 7;
						else
							mob[i].pattern = 8;
						SetTimer(hWnd, 4, 500, NULL);
						break;
					case 8:
						if (decision == 0)
							mob[i].pattern = 3;
						else if (decision == 1)
							mob[i].pattern = 4;
						else if (decision == 2)
							mob[i].pattern = 5;
						else
							mob[i].pattern = 6;
						SetTimer(hWnd, 4, 500, NULL);
						break;
					case 9:
						if (decision == 0)
							mob[i].pattern = 3;
						else if (decision == 1)
							mob[i].pattern = 4;
						else if (decision == 2)
							mob[i].pattern = 5;
						else
							mob[i].pattern = 6;
						SetTimer(hWnd, 4, 500, NULL);
						break;
					case 10:
						if (decision < 2)
							mob[i].pattern = buid(dre);
						else
							mob[i].pattern = 9;
						SetTimer(hWnd, 4, 500, NULL);
						break;
					case 20:
						if (decision < 2)
							mob[i].pattern = buid(dre);
						else
							mob[i].pattern = 9;
						SetTimer(hWnd, 4, 500, NULL);
						break;
					}
				}
			}
			break;
		// just회피 타이머
		case 6:
				warrior.just = false;
				mjust = false;
				KillTimer(hWnd, 6);
			break;
			// 스킬 회복 타이머
		case 7:
			if (warrior.mp < 10) {
				warrior.mp++;
			}
			break;
			// just 출력 타이머
		case 8:
			if (justout) {
				if (just.y >= 325) {
					just.y -= 5;
				}
				else {
					justout = false;
					just.y = 375;
					KillTimer(hWnd, 8);
				}
			}
			if (mjustout) {
				if (monjust.y >= 325) {
					monjust.y -= 5;
				}
				else {
					mjustout = false;
					monjust.y = 375;
					KillTimer(hWnd, 8);
				}
			}
			break;
			// 필살기 사용시간
		case 9:
			warrior.specialon = false;
			warrior.special = 0;
			KillTimer(hWnd, 9);
			break;
			// CHANCE 좌표
		case 10:
			if (warrior.specialon)
				chance.y--;
			else {
				chance.y = 375;
				KillTimer(hWnd, 10);
			}
			break;
			// 필살기 & 공격을 퍼부으세요
		case 11:
			for (int i = 0; i < 30; ++i) {
				mob[i].stun = false;
			}
			AD = false;
			SetTimer(hWnd, 5, 5000, NULL);
			KillTimer(hWnd, 11);
			break;
		case 12:
			if (warrior.location.y == 375) {
				if (warrior.location.x >= 200 && warrior.location.x < 900 && warrior.Adirection == RIGHT) {
					warrior.location.x += 70;
				}
				else if (warrior.location.x == 900 && warrior.Adirection == RIGHT) {
					for (int i = 0; i < 30; ++i) {
						if (mob[i].alive && !mob[i].attack) {
							Cattack(&warrior, &mob[i]);
							SetTimer(hWnd, 14, 50, NULL);
							if (!mob[i].alive) {
								SetTimer(hWnd, 1, 3000, NULL);				// 죽었을 때 몬스터 생성 타이머 다시 돌림
							}
						}
					}
					warrior.Adirection = LEFT;
					warrior.motion = 2;
				}
				else if (warrior.location.x > 200 && warrior.location.x <= 900 && warrior.Adirection == LEFT) {
					warrior.location.x -= 70;
					warrior.motion = 1;
				}
				else if (warrior.location.x == 200 && warrior.Adirection == LEFT)
					warrior.Adirection = STOP;
				else if (warrior.Adirection == STOP) {
					warrior.behavior = false;
					KillTimer(hWnd, 12);
					warrior.motion = 0;
					warrior.attack = false;
				}
			}
			break;

		case 13:
			if (!warrior.alive) {
				if (stage == 1) {
					mciSendCommand(dwID3, MCI_CLOSE, 0, NULL);
				}
				if (stage == 2) {
					mciSendCommand(dwID4, MCI_CLOSE, 0, NULL);
				}
				mciOpen.lpstrElementName = TEXT("GameOver.mp3");
				mciSendCommand(0, MCI_OPEN, MCI_OPEN_ELEMENT | MCI_OPEN_TYPE, (DWORD)(LPVOID)& mciOpen);
				dwID2 = mciOpen.wDeviceID;
				mciSendCommand(dwID2, MCI_PLAY, MCI_DGV_PLAY_REPEAT, (DWORD)(LPVOID)& mciPlay);
				start = false;
				gameover = true;
			}
			KillTimer(hWnd, 13);
			break;
			// 화면 흔들림
		case 14:
			if (x == 0) {
				x -= 3;
			}
			else {
				x += 3;
				count++;
			}
				if (count == 5) {
					count = 0;
					KillTimer(hWnd, 14);
				}

			break;
			// 클리어시 종료
		case 15:
			if (warrior.stage == 20)
				PostQuitMessage(0);
			break;
			// 힐 버프 끝 (공격력 떨어짐)
		case 16:
			warrior.damage /= 1.5;
			KillTimer(hWnd, 16);
			break;
			// 힐 버프 끝 (방어력 떨어짐)
		case 17:
			warrior.def /= 15;
			KillTimer(hWnd, 17);
			break;
		case 18:	// 연속 공격 타이머
			SetTimer(hWnd, 18, 2200, NULL);

			if (continuous_attack) {
				for (int i = 9; i <= 19; i += 10) {
					if (mob[i].alive) {
						if (temp == RIGHT) {
							if (warrior.dodge != RIGHT) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}
						if (temp == LEFT) {
							if (warrior.dodge != LEFT) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1; 
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}
						if (temp == UP) {
							if (warrior.dodge != UP) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}
						if (temp == DOWN) {
							if (warrior.dodge != DOWN) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}

					}
				}
				KillTimer(hWnd, 18);
			}
			else {
				temp = uid(dre) + 1;

				if (temp == RIGHT)
					right = true;
				if (temp == LEFT)
					left = true;
				if (temp == UP)
					up = true;
				if (temp == DOWN)
					down = true;

				SetTimer(hWnd, 22, 400, NULL);
			}

			break;
		case 19:	// 연속 공격 타이머
			SetTimer(hWnd, 19, 2200, NULL);
			if (continuous_attack) {
				for (int i = 9; i <= 19; i += 10) {
					if (mob[i].alive) {
						if (temp1 == RIGHT) {
							if (warrior.dodge != RIGHT) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}
						if (temp1 == LEFT) {
							if (warrior.dodge != LEFT) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}
						if (temp1 == UP) {
							if (warrior.dodge != UP) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}
						if (temp1 == DOWN) {
							if (warrior.dodge != DOWN) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}

					}
				}
				KillTimer(hWnd, 19);
			}
			else {
				temp1 = uid(dre) + 1;


				if (temp1 == RIGHT)
					right = true;
				if (temp1 == LEFT)
					left = true;
				if (temp1 == UP)
					up = true;
				if (temp1 == DOWN)
					down = true;
				
				SetTimer(hWnd, 22, 400, NULL);

			}
			break;
		case 20:	// 연속 공격 타이머
			SetTimer(hWnd, 20, 2200, NULL);
			if (continuous_attack) {
				for (int i = 9; i <= 19; i += 10) {
					if (mob[i].alive) {
						if (temp2 == RIGHT) {
							if (warrior.dodge != RIGHT) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}
						if (temp2 == LEFT) {
							if (warrior.dodge != LEFT) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}
						if (temp2 == UP) {
							if (warrior.dodge != UP) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}
						if (temp2 == DOWN) {
							if (warrior.dodge != DOWN) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}

					}
				}
				KillTimer(hWnd, 20);
			}
			else {
				temp2 = uid(dre) + 1;

				
				if (temp2 == RIGHT)
					right = true;
				if (temp2 == LEFT)
					left = true;
				if (temp2 == UP)
					up = true;
				if (temp2 == DOWN)
					down = true;

				SetTimer(hWnd, 22, 400, NULL);
			}
			break;
		case 21:	// 연속 공격 타이머
			SetTimer(hWnd, 21, 2200, NULL);

			if (continuous_attack) {
				for (int i = 9; i <= 19; i += 10) {
					if (mob[i].alive) {
						if (temp3 == RIGHT) {
							if (warrior.dodge != RIGHT) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}
						if (temp3 == LEFT) {
							if (warrior.dodge != LEFT) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}
						if (temp3 == UP) {
							if (warrior.dodge != UP) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}
						if (temp3 == DOWN) {
							if (warrior.dodge != DOWN) {
								Mcattack(&mob[i], &warrior);
								SetTimer(hWnd, 14, 50, NULL);
							}
							else {
								Mdelay = 1;
								justout = true;
								SetTimer(hWnd, 8, 50, NULL);
								SetTimer(hWnd, 3, Mdelay, NULL);
							}
						}

					}
				}
				continuous_attack = false;
				SetTimer(hWnd, 5, 3000, NULL);
				warrior.special++;
				if (warrior.special == 5) {
					SetTimer(hWnd, 9, 2000, NULL);
					warrior.specialon = true;
					SetTimer(hWnd, 10, 50, NULL);
				}
				KillTimer(hWnd, 21);
			}
			else {
				temp3 = uid(dre) + 1;

				if (temp3 == RIGHT)
					right = true;
				if (temp3 == LEFT)
					left = true;
				if (temp3 == UP)
					up = true;
				if (temp3 == DOWN)
					down = true;
				mob[9].attack = false;
				mob[19].attack = false;
				SetTimer(hWnd, 22, 400, NULL);
				continuous_attack = true;
			}
			break;
		case 22:
			right = false;
			up = false;
			down = false;
			left = false;
			KillTimer(hWnd, 22);
			break;
		case 23:

			if (sound_sec == 2) {
				mciSendCommand(dwID6, MCI_CLOSE, 0, NULL);
				sound_sec = 0;
				KillTimer(hWnd, 23);
				
				break;
			}
			else {
				sound_sec++;
			}
			break;
		}

		InvalidateRect(hWnd, NULL, false);
		break;
		
	case WM_DESTROY:
		PostQuitMessage(0);
		return 0;
	}
	return (DefWindowProc(hWnd, iMessage, wParam, lParam));
}
